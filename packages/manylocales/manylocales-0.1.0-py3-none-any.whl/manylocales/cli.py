# https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html
# https://www.gnu.org/software/gettext/manual/gettext.html
# https://polib.readthedocs.io/en/latest/

import os
import re
import sys
import json
import logging
import subprocess
import tempfile
import argparse
from typing import List, Optional
from dataclasses import dataclass, asdict, field
from pathlib import Path

import polib
import yaml

from .constants import LOCALES_BY_CODE


logger = logging.getLogger(__name__)


class ManyLocalesError(Exception):
    pass


DEFAULT_SYSTEM_PROMPT = (
    "You are a professional translator. "
    "You are given a PO file and you need to translate it to the given locale. "
    "You need to return the translated PO file content. "
    "Do not include any comments or other information in the output."
    "Do not include any code blocks (```) in the output."
    "Return only msgid (always), msgid_plural (if plural), msgstr (the same as in your input, fill all plural forms), msgctxt (if present)."
)


def validate_locale(locale):
    # ISO 639-1 2-letter code with optional 2-letter country code
    return re.match(r"[a-z]{2}(_[A-Z]{2})?", locale) is not None


GETTEXT_KEYWORDS = [
    "gettext",
    "gettext_noop",
    "gettext_lazy",
    "ngettext_lazy:1,2",
    "pgettext:1c,2",
    "npgettext:1c,2,3",
    "pgettext_lazy:1c,2",
    "npgettext_lazy:1c,2,3",
]


class Config:
    @classmethod
    def from_config(cls, config: dict):
        return cls(**{k: v for k, v in config.items() if k in cls.__annotations__})

    def to_dict(self):
        # Convert Paths to strings for serialization
        d = asdict(self)
        for k, v in d.items():
            if isinstance(v, Path):
                d[k] = str(v)
        return d

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_yaml(self):
        return yaml.dump(self.to_dict(), indent=4)


@dataclass
class GettextConfig(Config):
    domain: str = "messages"
    add_location: bool = True
    keywords: List[str] = field(default_factory=lambda: GETTEXT_KEYWORDS)


@dataclass
class ProjectConfig(Config):
    name: str
    type: str
    source: Path
    destination: Path
    origin_locale: str
    locales: List[str]
    description: Optional[str] = None
    gettext: GettextConfig = None

    def __post_init__(self):
        # Convert strings to Path objects if needed
        if isinstance(self.source, str):
            self.source = Path(self.source)
        if isinstance(self.destination, str):
            self.destination = Path(self.destination)
        if not validate_locale(self.origin_locale):
            raise ValueError(f"Invalid origin locale: {self.origin_locale}")
        for locale in self.locales:
            if not validate_locale(locale):
                raise ValueError(f"Invalid locale: {locale}")

    def is_file_supported(self, file_path):
        path_str = str(file_path) if isinstance(file_path, Path) else file_path
        if self.type == "gettext":
            return path_str.endswith((".py", ".js", ".jsx", ".ts", ".tsx"))
        elif self.type == "json":
            return path_str.endswith((".json"))
        else:
            raise ValueError(f"Unsupported project type: {self.type}")


class TranslationProvider:
    def translate(self, origin_locale: str, target_locale: str, text: str) -> str:
        raise NotImplementedError


@dataclass
class ProviderConfig(Config):
    type: str
    model: str
    temperature: float
    max_tokens: int
    system_prompt: str
    api_key: str = None
    cache: bool = False


def load_config(config_path: Optional[str] = None) -> List[ProjectConfig]:
    """Load and parse the manylocales.yaml file"""
    # Default config path is manylocales.yaml in current directory
    config_path = config_path or "manylocales.yaml"

    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing config file: {e}")
        sys.exit(1)

    # Extract global settings
    global_config = config.get("global", {})
    global_origin_locale = global_config.get("origin_locale", "en")
    global_locales = global_config.get("locales", ["en"])
    global_gettext = global_config.get("gettext", {})

    # Parse projects
    projects = []
    for project_name, project_config in config.get("projects", {}).items():
        # Merge global and project-specific settings
        origin_locale = project_config.get("origin_locale", global_origin_locale)
        locales = project_config.get("locales", global_locales)
        gettext_config = dict(global_gettext)
        gettext_config.update(project_config.get("gettext", {}))

        # Parse gettext config if project type is gettext
        gettext = None
        if project_config["type"] == "gettext":
            gettext = GettextConfig.from_config(gettext_config)

        # Create Project instance
        project = ProjectConfig(
            name=project_name,
            description=project_config.get("description"),
            type=project_config["type"],
            source=project_config["source"],
            destination=project_config["destination"],
            origin_locale=origin_locale,
            locales=locales,
            gettext=gettext
        )
        projects.append(project)

    # Parse provider config
    provider_config = config.get("provider", {})
    provider = ProviderConfig(
        type=provider_config.get("type", "chatgpt"),
        model=provider_config.get("model", "gpt-4o-mini"),
        temperature=provider_config.get("temperature", 0.1),
        max_tokens=provider_config.get("max_tokens", 4096),
        system_prompt=provider_config.get("system_prompt", DEFAULT_SYSTEM_PROMPT),
        cache=provider_config.get("cache", False),
    )

    return projects, provider


def handle_project(project: ProjectConfig, provider_config: ProviderConfig, from_scratch: bool):
    """Handle a single project"""
    logger.debug(f"Project: {project.name}")
    logger.debug(f"Config: {project.to_json()}")

    # Create provider
    provider = create_provider(provider_config, project.description)

    if project.type == "gettext":
        handler = GettextProjectHandler(project, provider, from_scratch)
        handler.handle()
    else:
        raise ValueError(f"Unsupported project type: {project.type}")


class GettextProjectHandler:
    def __init__(self, project: ProjectConfig, provider: TranslationProvider, from_scratch: bool):
        self.project = project
        self.provider = provider
        self.from_scratch = from_scratch

    def handle(self):
        # Get source files
        files = get_source_files(self.project)
        logger.debug(f"Source files:")
        for file in files:
            logger.debug(f" - {file}")
        if not files:
            logger.warning(f"No files found for project {self.project.name}")
            return

        collected_po_content = self._collect_messages(files)
        log_file_content(f"Collected PO file content for {self.project.name}", collected_po_content)

        # Translate messages for each locale
        for locale in self.project.locales:
            self._handle_locale(locale, collected_po_content)

    def _handle_locale(self, locale: str, collected_po_content: str):
        if locale == self.project.origin_locale:
            return
        logger.info(f"Processing locale: {self.project.name}/{locale}")

        # Merge with existing translations
        if self.from_scratch:
            merged_po_content = collected_po_content
        else:
            merged_po_content = self._merge_with_existing_translations(locale, collected_po_content)
            log_file_content(f"Merged PO file content for {self.project.name}/{locale}", merged_po_content)

        # Translate messages
        translated_po_content = self._translate_po_content(locale, merged_po_content)
        log_file_content(f"Translated PO file content for {self.project.name}/{locale}", translated_po_content)

        # Write result messages to output .po file
        po_path = self._get_po_path(locale)
        po_path.parent.mkdir(parents=True, exist_ok=True)
        with open(po_path, "w") as f:
            f.write(translated_po_content)

    def _get_po_path(self, locale: str):
        return Path(str(self.project.destination / (self.project.gettext.domain + ".po")).format(locale=locale))

    def _collect_messages(self, files: List[Path]):
        input_files = [str(file) for file in files]

        # Construct xgettext command
        command = [
            "xgettext",
            *[
                "--keyword={keyword}".format(keyword=keyword)
                for keyword in self.project.gettext.keywords
            ],
            "--from-code=utf-8",
            "--no-wrap",
            "--add-location" if self.project.gettext.add_location else "--no-location",
            # "-D",
            # project.source,
            "--output=-",
            *input_files,
        ]

        # Execute xgettext command
        messages = run(command)

        # Deduplicate messages
        command = [
            "msguniq",
            "--no-wrap",
            "-o",
            "-",
        ]
        po_content = run(command, stdin=messages)

        # Add metadata to the PO file
        po_file = polib.pofile(po_content)
        po_file.metadata["Language"] = self.project.origin_locale
        po_file.metadata["Content-Type"] = "text/plain; charset=UTF-8"
        if self.project.origin_locale in LOCALES_BY_CODE:
            po_file.metadata["Plural-Forms"] = LOCALES_BY_CODE[self.project.origin_locale][2]
        else:
            logger.warning(f"Plural-Forms metadata not found for locale: {self.project.origin_locale}")

        return str(po_file)

    def _merge_with_existing_translations(self, locale: str, po_content: str):
        po_path = self._get_po_path(locale)
        if po_path.exists():
            with tempfile.NamedTemporaryFile() as f:
                f.write(po_content.encode("utf-8"))
                f.flush()
                command = [
                    "msgmerge",
                    "-q",
                    "--previous",
                    "-o",
                    "-",
                    str(po_path),
                    f.name,
                ]
                return run(command, stdin=po_content)
        return po_content

    def _translate_po_content(self, locale: str, po_content: str):
        po_file = polib.pofile(po_content)
        if po_file.metadata.get("Language") != locale:
            po_file.metadata["Language"] = locale

        # Skip if already 100% translated
        if po_file.percent_translated() == 100:
            logger.info(f"{self.project.name}/{locale} is 100% translated, skipping")
            return po_content

        logger.info(f"Translating {self.project.name}/{locale}. {po_file.percent_translated()}% translated")

        # Translate
        translator = Translator(self.project.origin_locale, locale, po_file, self.provider)
        translated_po_file = translator.translate()

        # Remove obsolete entries
        for entry in translated_po_file.obsolete_entries():
            translated_po_file.remove(entry)

        translated_po_content = str(translated_po_file)

        # Translate messages
        logger.info(
            f"Finished translating {self.project.name}/{locale}. {translated_po_file.percent_translated()}% translated"
        )
        return translated_po_content


def get_source_files(project: ProjectConfig) -> List[Path]:
    """Get all input files from the project source that match supported extensions.

    Args:
        project: Project configuration

    Returns:
        List of Path objects for matching files
    """
    files = []

    # Handle source as a pattern
    source_str = str(project.source)
    if any(char in source_str for char in "*?[]"):
        matching_files = Path().glob(source_str)
        files.extend(path for path in matching_files if project.is_file_supported(path))
        return files

    # Handle single file
    if project.source.is_file():
        files.append(project.source)
        return files

    # Fallback to regular directory walk if no patterns
    try:
        for root, _, filenames in os.walk(project.source):
            for filename in filenames:
                if project.is_file_supported(filename):
                    files.append(Path(root) / filename)
    except Exception as e:
        logger.error(f"Error walking directory {project.source}: {e}")
        sys.exit(1)

    return files


def run(command, stdin=None):
    logger.debug(f"Executing command: {command} with stdin: {bool(stdin)}")

    for arg in command:
        assert isinstance(arg, str), f"Command argument {arg} is not a string"

    process = subprocess.Popen(
        command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = process.communicate(input=stdin.encode("utf-8") if stdin else None)
    if process.returncode != 0:
        logger.error(f"Error: {err}")
        sys.exit(1)
    return out.decode("utf-8")


class Translator:
    def __init__(
        self, origin_locale: str, target_locale: str, po_file: polib.POFile, provider: TranslationProvider
    ):
        self.origin_locale = origin_locale
        self.target_locale = target_locale
        self.po_file = po_file
        self.provider = provider

    def translate(self):
        # Check that we are not translating the same message twice
        translated_entry_ids = set()    # IDs of entries that were already sent to the provider
        skip_entry_ids = set()          # IDs of entries that were already sent to the provider, but still untranslated

        while True:
            # Get next batch
            batch_entries = self._get_batch(skip_entry_ids)
            if not batch_entries:
                break

            # Batch can contain both translated and untranslated entries. Here we get IDs of untranslated entries
            untranslated_batch_entry_ids = set(
                e.msgid_with_context for e in batch_entries if not e.translated()
            )
            # Add IDs of untranslated entries that were already sent to the provider
            skip_entry_ids |= untranslated_batch_entry_ids & translated_entry_ids

            # Translate batch
            batch_content = self._get_content_from_entries(batch_entries)
            translated_po_file = self.run_provider(batch_content)
            self._merge_translated_po_file(translated_po_file)
            translated_entry_ids.update(untranslated_batch_entry_ids)

        # Try to translate entries that were skipped
        if skip_entry_ids:
            untranslated_entries = [e for e in self.po_file if e.msgid_with_context in skip_entry_ids]
            untranslated_content = self._get_content_from_entries(untranslated_entries)
            translated_po_file = self.run_provider(untranslated_content)
            self._merge_translated_po_file(translated_po_file)

        return self.po_file

    def run_provider(self, batch_content: str) -> polib.POFile:
        logger.debug(f"Batch content:\n{batch_content}")
        response_content = ""
        try:
            response_content = self.provider.translate(self.origin_locale, self.target_locale, batch_content)
            logger.debug(f"Translated content:\n{response_content}")
            return polib.pofile(response_content)
        except IOError as e:
            logger.error(f"Error: {repr(e)}")
            raise
        except Exception as e:
            logger.error(
                f"Batch content:\n{batch_content}\nError: {e}"
            )
            raise ManyLocalesError(f"Error: {e}")

    def _get_batch(self, skip_entry_ids=None):
        skip_entry_ids = skip_entry_ids or set()

        # Find the most frequently used messages
        sorted_entries = sorted(
            self.po_file,
            key=lambda x: (-len(x.occurrences), x.linenum),
        )

        # Find untranslated entries
        untranslated_sorted_entries = [e for e in sorted_entries if not e.obsolete and not e.translated() and e.msgid_with_context not in skip_entry_ids]
        if not untranslated_sorted_entries:
            return []

        # Get all entries from the file with the most frequently used untranslated message
        try:
            src_filename = untranslated_sorted_entries[0].occurrences[0][0]
        except IndexError:
            src_filename = None

        src_entries = [
            e
            for e in self.po_file
            if (
                (
                    e.occurrences and e.occurrences[0][0] == src_filename
                )  # Entry from the same file
                or (
                    not e.occurrences and src_filename is None
                )  # Entries without file info
            )
        ]
        src_entries = sorted(
            src_entries,
            key=lambda x: x.linenum,
        )

        # TODO batch entries within the same file if batch size is too big
        # TODO batch entries from different files if batch size is too small

        return src_entries

    def _merge_translated_po_file(self, translated_po_file):
        entries_dict = {entry.msgid_with_context: entry for entry in self.po_file}
        for entry in translated_po_file:
            existing_entry = entries_dict.get(entry.msgid_with_context)
            if not existing_entry:
                continue
            if existing_entry.translated():
                continue

            # Remove fuzzy
            if existing_entry.fuzzy:
                existing_entry.fuzzy = False

            # Update existing entry
            existing_entry.msgstr = entry.msgstr

            # Update plural forms if present
            if existing_entry.msgid_plural:
                if existing_entry.msgid_plural != entry.msgid_plural:
                    raise ManyLocalesError(
                        f"Plural forms do not match: {existing_entry.msgid_plural} != {entry.msgid_plural}"
                    )

                for key in existing_entry.msgstr_plural:
                    if key in entry.msgstr_plural:
                        existing_entry.msgstr_plural[key] = entry.msgstr_plural[key]

    def _get_content_from_entries(self, entries):
        content = "\n".join(map(str, entries))
        return content


class ChatGPTTranslationProvider(TranslationProvider):
    def __init__(self, config: ProviderConfig, description: Optional[str] = None):
        from openai import OpenAI

        self.api_key = config.api_key
        self.model = config.model
        self.temperature = config.temperature
        self.max_tokens = config.max_tokens
        self.system_prompt = config.system_prompt
        self.client = OpenAI(api_key=self.api_key)
        self.description = description

    def translate(self, origin_locale: str, target_locale: str, text: str) -> str:
        """
        Translate the given PO file content using ChatGPT.
        """
        prompt = self.system_prompt
        if self.description:
            prompt = prompt + "\nTranslate in the context of the following project description: " + self.description
        messages = [
            {"role": "system", "content": prompt},
            {
                "role": "system",
                "content": (
                    "Original locale: {origin_locale}\n"
                    "Target locale: {target_locale}"
                ).format(
                    **{
                        "origin_locale": origin_locale,
                        "target_locale": target_locale,
                    }
                ),
            },
            {"role": "user", "content": text},
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        self.validate_response(response.choices[0].message.content)
        return response.choices[0].message.content

    def validate_response(self, response: str):
        if not response:
            raise ManyLocalesError("ChatGPT returned empty response")
        if "```" in response:
            raise ManyLocalesError("ChatGPT returned invalid response")


class CachingTranslationProvider(TranslationProvider):
    def __init__(self, translation_provider: TranslationProvider, cache_path: Path):
        self.translation_provider = translation_provider
        self.cache_path = cache_path
        self.cache = self._load_cache()

    def _load_cache(self):
        if self.cache_path.exists():
            with open(self.cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_path, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=4)

    def translate(self, origin_locale: str, target_locale: str, text: str) -> str:
        cache_key = f"{origin_locale}:{target_locale}:{text}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Proxy the translation request to the underlying provider
        translation = self.translation_provider.translate(origin_locale, target_locale, text)

        # Cache the result
        self.cache[cache_key] = translation
        self._save_cache()

        return translation


def create_provider(provider_config: ProviderConfig, description: Optional[str] = None) -> TranslationProvider:
    """Create a translation provider based on the configuration.

    Args:
        provider_config: Provider configuration object

    Returns:
        TranslationProvider instance

    Raises:
        ValueError: If provider type is not supported
    """
    provider = None
    if provider_config.type == "chatgpt":
        # Get API key from environment variable
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required for ChatGPT provider")

        provider_config.api_key = api_key
        provider = ChatGPTTranslationProvider(provider_config, description)
    else:
        raise ValueError(f"Unsupported provider type: {provider_config.type}")

    if provider_config.cache:
        provider = CachingTranslationProvider(provider, Path(".manylocales_cache") / f"{provider_config.type}.json")

    return provider


def setup_logging(verbose: bool):
    # Configure root logger to INFO level
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s" if verbose else "%(message)s",
        handlers=[logging.StreamHandler()]
    )

    # Set logger level based on verbose flag
    logger = logging.getLogger("manylocales")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)


def log_file_content(title: str, content: str):
    wrapped_content = "\n".join(f'┃ {line}' for line in content.splitlines())
    logger.debug(f"{title}\n{'┏' + '━' * 79}\n{wrapped_content}\n{'┗' + '━' * 79}\n\n")


def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(
        description="ManyLocales is a tool for automatic translations using AI."
    )
    parser.add_argument(
        "-w",
        "--workdir",
        help="Change current working directory to this directory before executing the command",
    )
    parser.add_argument("-c", "--config", help="Path to manylocales.yaml file")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose mode",
    )
    parser.add_argument(
        "--from-scratch",
        action="store_true",
        help="Don't reuse existing translations, translate everything from scratch",
    )
    args = parser.parse_args()

    # Set up logging
    setup_logging(args.verbose)

    # Change working directory if specified in CLI args
    if args.workdir:
        os.chdir(args.workdir)

    # Load config
    config_path = args.config
    projects, provider_config = load_config(config_path)

    # Run with parsed projects
    for project in projects:
        handle_project(project, provider_config, from_scratch=args.from_scratch)


def cli():
    try:
        main()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)


if __name__ == "__main__":
    cli()
