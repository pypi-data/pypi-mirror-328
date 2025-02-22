from enum import Enum


class InputFormat(str, Enum):
    """Available input formats for LLM scraping"""

    HTML = "html"
    MARKDOWN = "markdown"
    FIT_MARKDOWN = "fit_markdown"


class OutputFormat(str, Enum):
    """Available output formats for scraping"""

    HTML = "html"
    CLEANED_HTML = "cleaned_html"
    MARKDOWN = "markdown"
    FIT_MARKDOWN = "fit_markdown"


class CacheMode(str, Enum):
    """Cache control modes for the API requests"""

    BYPASS = "bypass"  # Skip cache for this request
    DISABLED = "disabled"  # Completely disable caching
    WRITE_ONLY = "write_only"  # Only write to cache, don't read
    READ_ONLY = "read_only"  # Only read from cache, don't write
