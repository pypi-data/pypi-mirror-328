"""
Async python client for interacting with the Crawl4AI Cloud API. (https://www.crawl4ai-cloud.com/)
"""

# Main client
from .client import Crawl4AICloudClient

# Exceptions
from .exceptions import (
    ScrapingError,
    ApiError,
)

# Enums
from .enums import InputFormat, OutputFormat, CacheMode

# Schemas
from .schemas import (
    JsonCssField,
    JsonCssSchema,
    ApiKey,
    UrlScrapingPayload,
    LlmInstructionPayload,
    JsonCssExtractionPayload,
    CssSchemaGeneratorPayload,
    JsonPayload,
    ResultSuccess,
    ResultSchema,
    ScrapingResult,
)

# helper utils
from .utils import (
    decode_base64,
    validate_base64,
)

__all__ = [
    # Main client
    "Crawl4AICloudClient",
    # Exceptions
    "ScrapingError",
    "ApiError",
    # Enums
    "InputFormat",
    "OutputFormat",
    "CacheMode",
    # Schemas
    "JsonCssField",
    "JsonCssSchema",
    "ApiKey",
    "UrlScrapingPayload",
    "LlmInstructionPayload",
    "JsonCssExtractionPayload",
    "CssSchemaGeneratorPayload",
    "JsonPayload",
    "ResultSuccess",
    "ResultSchema",
    "ScrapingResult",
    # helper func
    "decode_base64",
    "validate_base64",
]


__version__ = "1.0.0"
