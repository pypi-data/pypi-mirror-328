from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    SecretStr,
    ConfigDict,
    field_validator,
)

from typing import (
    Dict,
    List,
    Optional,
    Union,
    Literal,
    Any,
)

from .enums import (
    OutputFormat,
    CacheMode,
    InputFormat,
)
from .utils import validate_base64


class ApiKey(BaseModel):
    """API key for authentication with enhanced security"""

    apikey: SecretStr = Field(
        description="API key for authentication",
        min_length=20,
        max_length=20,
    )

    def get_secret_value(self) -> str:
        """Safely retrieve the API key value"""
        return self.apikey.get_secret_value()

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "apikey": "709b1fd99b8dd227fed4",
            }
        }
    )


class BasicScrapingPayload(BaseModel, use_enum_values=True):
    """Base payload schema for all scraping requests"""

    url: HttpUrl = Field(..., description="Target webpage URL")
    output_format: Optional[OutputFormat] = Field(
        default=OutputFormat.MARKDOWN,
        description="""Optional parameter that specifies which formatting will be used for result output. 
                       By default, output_format is set to "markdown". 
                       Other possible settings: "cleaned_html", "fit_markdown" or "html". """,
    )
    cache_mode: Optional[CacheMode] = Field(
        default=CacheMode.BYPASS,
        description="Optional parameter that controls caching behavior for content retrieval.",
    )
    js_code: Optional[str] = Field(
        None,
        description="Execute custom JavaScript code on the target page before extraction",
    )
    magic: Optional[bool] = Field(
        None,
        description="Enable comprehensive anti-bot protection bypass with the magic parameter.",
    )
    process_iframes: Optional[bool] = Field(
        None, description="Enable crawling of content within iframes."
    )
    remove_overlay_elements: Optional[bool] = Field(
        None,
        description="Remove popups, ads, and other overlay elements during crawling.",
    )
    excluded_tags: Optional[List[str]] = Field(
        None, description="Filter out specific HTML elements during content extraction."
    )
    wait_for: Optional[str] = Field(
        None,
        description="Specify CSS/XPath selector elements to wait for before processing the page.",
    )
    css_selector: Optional[str] = Field(
        None,
        description="Focus content extraction on specific page elements with CSS selector.",
    )
    word_count_threshold: Optional[int] = Field(
        None, description="Filter content blocks based on minimum word count."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "url": "https://example.com",
                "apikey": "your_api_key",
                "output_format": "markdown",
                "js_code": """window.scrollTo(0, document.body.scrollHeight);
                              document.querySelector('#fr-submit-btn').click();""",
                "cache_mode": "bypass",
                "excluded_tags": ["nav", "footer"],
                "magic": True,
            }
        }
    )


class UrlScrapingPayload(BasicScrapingPayload, use_enum_values=True):
    """
    Payload schema for URL scraping requests. Includes screenshot.

    Screenshot Features:

    ✓ Capture full page screenshots
    ✓ Optional delay before capture
    ✓ Returns base64 encoded PNG
    ✓ Perfect for visual verification

    Use screenshot_wait_for parameter to ensure dynamic content is loaded

    Note: Due to payload size and latency considerations,
    LLM extraction and JSON-CSS extraction will be disabled when screenshot is enabled.

    """

    screenshot: Optional[bool] = Field(
        None, description="Whether to capture screenshot."
    )
    screenshot_wait_for: Optional[float] = Field(
        None, description="Optional delay for capturing screenshot."
    )

    model_config = ConfigDict(
        use_enum_values=True,
        json_schema_extra={
            "example": {
                "url": "https://example.com",
                "apikey": "your_api_key",
                "output_format": "markdown",
                "cache_mode": "bypass",
                "excluded_tags": ["nav", "footer"],
                "magic": True,
                "js_code": """
                    (async () => {
                        const tabs = document.querySelectorAll("section.charge-methodology .tabs-menu-3 > div");
            
                        for(let tab of tabs) {
                            // scroll to the tab
                            tab.scrollIntoView();
                            tab.click();
                            // Wait for content to load and animations to complete
                            await new Promise(r => setTimeout(r, 500));
                        }
                    })();
                    """,
                "screenshot": True,
                "screenshot_wait_for": 0.1,
            }
        },
    )


class LlmInstructionPayload(BasicScrapingPayload):
    """Payload schema for LLM instruction and schema requests."""

    llm_schema: Optional[Dict[str, str]] = Field(
        description="Dictionary mapping field names to their descriptions"
    )
    llm_instruction: str = Field(
        description="Natural language prompt for extraction (max 200 tokens)",
    )
    input_format: Optional[InputFormat] = Field(
        InputFormat.MARKDOWN,
        description="""Optional parameter that specifies which page content is fed to the LLM for extraction. 
                       By default, input_format is set to "markdown", meaning the page's markdown is fed to the LLM. 
                       You can also set the parameter to "fit_markdown" or "html". The "fit_markdown" setting 
                       in particular can drastically reduce the number of tokens sent to LLMs 
                       (if you trust the underlying markdown filtering logic).""",
    )


class JsonCssField(BaseModel):
    """Field definition for JSON CSS extraction"""

    name: str = Field(description="Name of the field to extract")
    selector: str = Field(description="CSS selector to locate the field")
    type: str = Field(description="Type of extraction (e.g., 'text', 'attribute')")
    attribute: Optional[str] = Field(
        default=None,
        description="Attribute name to extract (required when type is 'attribute')",
    )


class JsonCssSchema(BaseModel):
    """Schema for JSON CSS-based extraction"""

    name: str = Field(description="Name of the schema")
    base_selector: str = Field(
        description="Base CSS selector for repeating elements",
        alias="baseSelector",
    )
    fields: List[JsonCssField] = Field(description="List of fields to extract")

    model_config = ConfigDict(populate_by_name=True)


class JsonCssExtractionPayload(UrlScrapingPayload, use_enum_values=True):
    """Payload schema for Json CSS extraction strategy"""

    json_css_schema: JsonCssSchema = Field(
        None, description="JSON Extraction schema using CSS selectors"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "url": "https://example.com",
                "apikey": "your_api_key",
                "output_format": "markdown",
                "cache_mode": "bypass",
                "excluded_tags": ["nav", "footer"],
                "magic": True,
                "json_css_schema": {
                    "name": "KidoCode Courses",
                    "baseSelector": "section.charge-methodology .div-block-214.p-extraxx",
                    "fields": [
                        {
                            "name": "section_title",
                            "selector": "h3.heading-50",
                            "type": "text",
                        },
                        {
                            "name": "section_description",
                            "selector": ".charge-content",
                            "type": "text",
                        },
                        {
                            "name": "course_name",
                            "selector": ".text-block-93",
                            "type": "text",
                        },
                        {
                            "name": "course_description",
                            "selector": ".course-content-text",
                            "type": "text",
                        },
                        {
                            "name": "course_icon",
                            "selector": ".image-92",
                            "type": "attribute",
                            "attribute": "src",
                        },
                    ],
                },
            }
        }
    )


class Link(BaseModel):
    """Represents a scraped link"""

    href: str
    text: str
    type: Literal["external", "internal"]


class Image(BaseModel):
    """Represents a scraped image"""

    src: HttpUrl
    alt: str
    type: Literal["image"] = Field("image", exclude=True)
    relevance_score: int


class Media(BaseModel):
    """Base class for media types"""

    src: HttpUrl
    # todo change when duration type will be known, likely float
    duration: Any


class Audio(BaseModel):
    """Represents audio content"""

    type: Literal["audio"] = "audio"


class Video(BaseModel):
    """Represents video content"""

    type: Literal["video"] = "video"


class Metadata(BaseModel):
    """Page metadata model"""

    # Basic metadata
    title: Optional[str] = Field(None, exclude=False)
    description: Optional[str] = Field(None, alias="og:title")
    keywords: Optional[str] = Field(None, alias="og:title")
    author: Optional[str] = Field(None, alias="og:title")

    # Open Graph metadata
    og_title: Optional[str] = Field(None, alias="og:title")
    og_type: Optional[str] = Field(None, alias="og:type")
    og_url: Optional[HttpUrl] = Field(None, alias="og:url")
    og_description: Optional[str] = Field(None, alias="og:description")
    og_image: Optional[HttpUrl] = Field(None, alias="og:image")

    # Other common metadata
    robots: Optional[str] = None
    viewport: Optional[str] = None
    charset: Optional[str] = None
    language: Optional[str] = None
    canonical: Optional[HttpUrl] = None
    generator: Optional[str] = None
    theme_color: Optional[str] = None
    twitter_card: Optional[str] = Field(None, alias="twitter:card")
    twitter_site: Optional[str] = Field(None, alias="twitter:site")
    twitter_creator: Optional[str] = Field(None, alias="twitter:creator")
    twitter_title: Optional[str] = Field(None, alias="twitter:title")
    twitter_description: Optional[str] = Field(None, alias="twitter:description")
    twitter_image: Optional[HttpUrl] = Field(None, alias="twitter:image")

    model_config = ConfigDict(populate_by_name=True)


class CssSchemaGeneratorPayload(BaseModel):
    """
    Don't want to manually create JSON CSS schema? You can use this utility/helper API to turn raw HTML content
    into the corresponding JSON CSS schema.
    """

    html: str = Field(
        examples=[
            """
        <div class="product-card">
            <h2 class="title">Gaming Laptop</h2>
            <div class="price">$999.99</div>
            <div class="specs">
                <ul>
                    <li>16GB RAM</li>
                    <li>1TB SSD</li>
                </ul>
            </div>
        </div>
        """
        ]
    )
    utility_mode: Literal["json_css_schema_generator"] = "json_css_schema_generator"


JsonPayload = Union[
    UrlScrapingPayload,
    LlmInstructionPayload,
    JsonCssExtractionPayload,
    CssSchemaGeneratorPayload,
]


# Responses
class ResultSuccess(BaseModel):
    content: Optional[str] = None
    links: List[Link] = Field(
        default_factory=list, description="List of found links: url, email, tel"
    )
    images: List[Image] = Field(
        default_factory=list,
        description="List of found images, each includes src url, alt tag, relevance_score",
    )
    videos: List[Video] = Field(
        default_factory=list,
        description="List of found videos, each includes url and duration",
    )
    audios: List[Audio] = Field(
        default_factory=list,
        description="List of found audios, each includes url and duration",
    )
    metadata: Metadata = Field(description="Information from metadata")
    screenshot: str = Field(
        default="DISABLED", description="Either 'DISABLED' or a base64 encoded string"
    )
    extractions: List = Field(
        default_factory=list, description="List of extraction results"
    )

    @field_validator("screenshot")
    def validate_screenshot(cls, v):
        if v == "DISABLED":
            return "DISABLED"
        if not validate_base64(v):
            raise ValueError(
                'screenshot must be either "DISABLED" or a valid base64 encoded string'
            )
        return v

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "content": "some text",
                "links": [
                    {
                        "href": "https://www.iana.org/domains/example",
                        "text": "More information...",
                        "type": "external",
                    },
                    {
                        "href": "https://www3.weforum.org/docs/WEF_FOJ_Executive_Summary_Jobs.pdf",
                        "text": "Read article",
                        "type": "external",
                    },
                    {
                        "href": "tel:+60122020797",
                        "text": "+60122020797 (Sales team)",
                        "type": "external",
                    },
                ],
                "images": [
                    {
                        "src": "https://cdn.prod.website-files.com/61d6943d6b5924685ac825ca/64a6a1218fmark-white.svg",
                        "alt": "coding school for kids",
                        "relevance_score": 4,
                    },
                    {
                        "src": "https://cdn.prod.website-files.com/61d6943d6b59241863c825d6/663dfd4378eing868883.jpg",
                        "alt": "",
                        "relevance_score": 5,
                    },
                ],
                "videos": [],
                "audios": [
                    {
                        "src": "https://kidocode.com/gruppa_rozhdestvo_tak_hochetsya_zhit_1.mp3",
                        "type": "audio",
                        "duration": None,
                    },
                    {
                        "src": "https://kidocode.com/atc_around_the_world_1.mp3",
                        "type": "audio",
                        "duration": None,
                    },
                ],
                "metadata": {
                    "title": "Technology Degree For Kids in Malaysia - Kidocode",
                    "description": "Empower your child with a unique Information Technology",
                    "keywords": "technology courses, technology school, school for kids, best school malaysia",
                    "author": "Kidocode",
                    "og:title": "KidoCode - Computer Programming Course for Kids & Teens",
                    "og:type": "website",
                    "og:url": "https://www.kidocode.com",
                    "og:description": "Computer programming and mathematics school for primary school.",
                    "og:image": "https://kidocode-asset.s3.ap-southeast-1.amazonaws.com/website/images/poster.png",
                },
                "screenshot": "DISABLED",
                "extractions": [
                    {
                        "course_name": "Coding with Python",
                        "course_description": "Explore the exciting intersection of art and technology with Python.",
                        "error": False,
                    },
                    {
                        "course_name": "Electronics & Robotics",
                        "course_description": "Electronics and Robotics is a foundational course.",
                        "error": False,
                    },
                    {
                        "course_name": "Beginner Electronics Programming",
                        "course_description": "Learn basic concepts of electronics and circuits!",
                        "error": False,
                    },
                ],
            }
        }
    )


class ResultSchema(BaseModel):
    # using alias to avoid waring:
    #   UserWarning: Field name "schema" in "ResultSchema" shadows an attribute in parent "BaseModel"
    extraction_schema: JsonCssSchema = Field(alias="schema")
    model_config = ConfigDict(populate_by_name=True)


ScrapingResult = Union[ResultSuccess, ResultSchema]
