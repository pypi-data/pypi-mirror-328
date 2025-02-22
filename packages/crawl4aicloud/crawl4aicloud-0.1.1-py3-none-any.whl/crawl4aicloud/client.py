import aiohttp
from pydantic import HttpUrl
from typing import (
    List,
    Optional,
    Dict,
)

from .schemas import (
    UrlScrapingPayload,
    LlmInstructionPayload,
    JsonCssExtractionPayload,
    CssSchemaGeneratorPayload,
    JsonPayload,
    JsonCssSchema,
    ResultSuccess,
    ResultSchema,
    ScrapingResult,
)

from .enums import (
    CacheMode,
    InputFormat,
    OutputFormat,
)

from .exceptions import (
    ScrapingError,
    ApiError,
)

# Constants
DEFAULT_TIMEOUT = 30.0  # Default timeout in seconds
DEFAULT_API_URL = "https://www.crawl4ai-cloud.com/query"


class Crawl4AICloudClient:
    """
    Async client for the Crawl4AI web scraping API.

    Examples:

        # Using with context manager:
        async with Crawl4AICloudClient(api_key="your_key") as client:
            result = await client.basic_scrape(url="https://example.com")

        # Using without context manager:
        client = Crawl4AICloudClient(api_key="your_key")
        try:
            await client.connect()
            result = await client.basic_scrape(url="https://example.com")
        except ScrapingError as e:
            print(f"Scraping failed: {e}")
        finally:
            await client.close()
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_url: str = DEFAULT_API_URL,
        timeout: float = DEFAULT_TIMEOUT,
    ):
        """
        Initialize the Crawl4AI client.

        Args:
            api_key: API key for authentication
            api_url: Base API URL
            timeout: Request timeout in seconds

        Raises:
            ValueError: If API key format is invalid
        """
        self.api_key = api_key

        # Validate API key format
        if not len(self.api_key) == 20:
            raise ValueError("API key must be 20 characters long")

        self.api_url = api_url or DEFAULT_API_URL
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self._session = None

    async def connect(self) -> None:
        """
        Initialize the aiohttp session.
        Call this if not using the context manager.
        """
        if self._session is None:
            self._session = aiohttp.ClientSession(timeout=self.timeout)

    async def close(self) -> None:
        """
        Close the aiohttp session.
        Call this if not using the context manager.
        """
        if self._session:
            await self._session.close()
            self._session = None

    async def __aenter__(self):
        """Set up async context manager"""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Clean up async context manager"""
        await self.close()

    async def _ensure_session(self):
        """Ensure session exists before making requests"""
        if self._session is None:
            await self.connect()

    async def _request(
        self,
        payload: JsonPayload,
    ) -> ScrapingResult:
        """
        Make an API request with the given payload.

        Args:
            payload: Request payload

        Returns:
            ScrapingResult: Successful scraping result

        Raises:
            ScrapingError: If the scraping result returns {"error": ""}
            ApiError: If network error occurs
        """
        await self._ensure_session()

        # Prepare request payload
        json = payload.model_dump(
            mode="json",
            by_alias=True,
            exclude_none=True,
        )
        json["apikey"] = self.api_key

        try:
            async with self._session.post(self.api_url, json=json) as response:
                response.raise_for_status()
                result = await response.json()

                if result.get("error"):
                    raise ScrapingError(result["error"])

                # json css extraction schema request
                if result.get("schema"):
                    return ResultSchema(**result)

                if not result.get("content"):
                    raise ScrapingError(
                        "Empty response returned. Target website might be down or you have provided wrong URL."
                    )

                # usual request
                return ResultSuccess(**result)

        except aiohttp.ClientError as e:
            raise ApiError(f"Request failed: {e}")

    async def basic_scrape(
        self,
        url: HttpUrl,
        *,
        output_format: Optional[OutputFormat] = None,
        cache_mode: Optional[CacheMode] = None,
        js_code: Optional[str] = None,
        magic: Optional[bool] = None,
        process_iframes: Optional[bool] = None,
        remove_overlay_elements: Optional[bool] = None,
        excluded_tags: List[str] = None,
        wait_for: Optional[str] = None,
        css_selector: Optional[str] = None,
        word_count_threshold: Optional[int] = None,
        screenshot: Optional[bool] = None,
        screenshot_wait_for: Optional[float] = None,
    ) -> ScrapingResult:
        """
        Perform basic web scraping.

        Args:
            url: Target webpage URL
            output_format: Output format (html, cleaned_html, markdown, fit_markdown)
            cache_mode: Cache control mode. Enum: bypass, disabled, write_only, read_only
            js_code: Execute custom JavaScript code on the target page before extraction
            magic: Enable comprehensive anti-bot protection bypass with the magic parameter
            process_iframes: Enable crawling of content within iframes
            remove_overlay_elements: Remove popups, ads, and other overlay elements during crawling
            excluded_tags: Filter out specific HTML elements during content extraction
            wait_for: Specify CSS/XPath selector elements to wait for before processing the page
            css_selector: Focus content extraction on specific page elements with CSS selector
            word_count_threshold: Filter content blocks based on minimum word count
            screenshot: Whether to capture screenshot
            screenshot_wait_for: Optional delay for capturing screenshot

        Returns:
            ScrapingResult: Scraping results including content and metadata

        Raises:
            ScrapingError: If the scraping result returns {"error": ""}
            ApiError: If network error occurs
        """
        payload = UrlScrapingPayload(
            url=url,
            output_format=output_format,
            cache_mode=cache_mode,
            js_code=js_code,
            magic=magic,
            process_iframes=process_iframes,
            remove_overlay_elements=remove_overlay_elements,
            excluded_tags=excluded_tags,
            wait_for=wait_for,
            css_selector=css_selector,
            word_count_threshold=word_count_threshold,
            screenshot=screenshot,
            screenshot_wait_for=screenshot_wait_for,
        )

        return await self._request(payload)

    async def llm_extract(
        self,
        url: HttpUrl,
        llm_instruction: str,
        llm_schema: Optional[Dict[str, str]] = None,
        input_format: Optional[InputFormat] = None,
        *,
        output_format: Optional[OutputFormat] = None,
        cache_mode: Optional[CacheMode] = None,
        js_code: Optional[str] = None,
        magic: Optional[bool] = None,
        process_iframes: Optional[bool] = None,
        remove_overlay_elements: Optional[bool] = None,
        excluded_tags: List[str] = None,
        wait_for: Optional[str] = None,
        css_selector: Optional[str] = None,
        word_count_threshold: Optional[int] = None,
    ) -> ScrapingResult:
        """
        Extract structured data using LLM instructions and optional schema definitions.

        Args:
            url: Target webpage URL
            llm_instruction: Natural language prompt for extraction (max 200 tokens)
            llm_schema: Optional dictionary defining expected fields and their descriptions
            input_format: Optional parameter that specified which page content is fed to the LLM for extraction. By
                          default, input_format is set to "markdown", meaning the page's markdown is fed to the LLM.
                          You can also set the parameter to "fit_markdown" or "html". The "fit_markdown" setting in
                          particular can drastically reduce the number of tokens sent to LLMs (if you trust the
                          underlying markdown filtering logic). Enum: markdown, fit_markdown, html
            output_format: Output format. Enum: html, cleaned_html, markdown, fit_markdown
            cache_mode: Cache control mode. Enum: bypass, disabled, write_only, read_only
            js_code: Execute custom JavaScript code on the target page before extraction
            magic: Enable comprehensive anti-bot protection bypass with the magic parameter
            process_iframes: Enable crawling of content within iframes
            remove_overlay_elements: Remove popups, ads, and other overlay elements during crawling
            excluded_tags: Filter out specific HTML elements during content extraction
            wait_for: Specify CSS/XPath selector elements to wait for before processing the page
            css_selector: Focus content extraction on specific page elements with CSS selector
            word_count_threshold: Filter content blocks based on minimum word count

        Returns:
            ScrapingResult: Extraction results

        Raises:
            ScrapingError: If the scraping request returns {"error": ""} or request failed.
        """
        payload = LlmInstructionPayload(
            url=url,
            llm_instruction=llm_instruction,
            llm_schema=llm_schema,
            input_format=input_format,
            output_format=output_format,
            cache_mode=cache_mode,
            js_code=js_code,
            magic=magic,
            process_iframes=process_iframes,
            remove_overlay_elements=remove_overlay_elements,
            excluded_tags=excluded_tags,
            wait_for=wait_for,
            css_selector=css_selector,
            word_count_threshold=word_count_threshold,
        )

        return await self._request(payload)

    async def json_css_extract(
        self,
        url: HttpUrl,
        json_css_schema: JsonCssSchema,
        *,
        output_format: Optional[OutputFormat] = None,
        cache_mode: Optional[CacheMode] = None,
        js_code: Optional[str] = None,
        magic: Optional[bool] = None,
        process_iframes: Optional[bool] = None,
        remove_overlay_elements: Optional[bool] = None,
        excluded_tags: List[str] = None,
        wait_for: Optional[str] = None,
        css_selector: Optional[str] = None,
        word_count_threshold: Optional[int] = None,
    ) -> ScrapingResult:
        """
        The JSON-CSS-based extraction is a powerful feature of Crawl4AI that allows you to extract structured data
        from web pages using CSS selectors. This method is particularly useful when you need to extract specific
        data points from a consistent HTML structure, such as tables or repeated elements. Here's how to use it
        with the AsyncWebCrawler. All you need is to define a schema that specifies: 1. A base CSS selector for
        the repeating elements 2. Fields to extract from each element, each with its own CSS selector.
        This strategy is fast and efficient, as it doesn't rely on external services like LLMs for extraction.

        Args:
            url: Target webpage URL
            json_css_schema: Json schema with css selectors,
            output_format: Output format. Enum: html, cleaned_html, markdown, fit_markdown
            cache_mode: Cache control mode. Enum: bypass, disabled, write_only, read_only
            js_code: Execute custom JavaScript code on the target page before extraction
            magic: Enable comprehensive anti-bot protection bypass with the magic parameter
            process_iframes: Enable crawling of content within iframes
            remove_overlay_elements: Remove popups, ads, and other overlay elements during crawling
            excluded_tags: Filter out specific HTML elements during content extraction
            wait_for: Specify CSS/XPath selector elements to wait for before processing the page
            css_selector: Focus content extraction on specific page elements with CSS selector
            word_count_threshold: Filter content blocks based on minimum word count
        """
        payload = JsonCssExtractionPayload(
            url=url,
            json_css_schema=json_css_schema,
            output_format=output_format,
            cache_mode=cache_mode,
            js_code=js_code,
            magic=magic,
            process_iframes=process_iframes,
            remove_overlay_elements=remove_overlay_elements,
            excluded_tags=excluded_tags,
            wait_for=wait_for,
            css_selector=css_selector,
            word_count_threshold=word_count_threshold,
            screenshot=None,
            screenshot_wait_for=None,
        )

        return await self._request(payload)

    async def json_css_schema_generator(
        self,
        html: str,
    ) -> ScrapingResult:
        """
        While manually crafting schemas is powerful and precise, Crawl4AI now offers a convenient utility to automatically generate extraction schemas using LLM. This is particularly useful when:

        You're dealing with a new website structure and want a quick starting point
        You need to extract complex nested data structures
        You want to avoid the learning curve of CSS/XPath selector syntax

        Benefits of Schema Generation

        - One-Time Cost: While schema generation uses LLM, it's a one-time cost. The generated schema can be reused for unlimited extractions without further LLM calls.
        - Smart Pattern Recognition: The LLM analyzes the HTML structure and identifies common patterns, often producing more robust selectors than manual attempts.
        - Automatic Nesting: Complex nested structures are automatically detected and properly represented in the schema.
        - Learning Tool: The generated schemas serve as excellent examples for learning how to write your own schemas.

        Args:
            html: Raw HTML content

        Returns:
            ScrapingResult: Generated schema

        Raises:
            ScrapingError: If the scraping result returns {"error": ""}
            ApiError: If network error occurs
        """
        payload = CssSchemaGeneratorPayload(
            html=html,
            utility_mode="json_css_schema_generator",
        )

        return await self._request(payload)
