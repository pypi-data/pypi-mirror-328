# crawl4aicloud is python async client for  [crawl4ai-cloud API](https://www.crawl4ai-cloud.com/)

## Installation
with pip:

`pip install crawl4aicloud`

or with uv:

`uv pip install crawl4aicloud`


### How to use:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient, ScrapingError, ApiError


url = "https://www.kidocode.com/degrees/technology"

llm_instruction = """Extract the course name of each item listed in the 
                    "Explore our future-forward courses" section. 
                    The extraction should look like: 
                    {'course_name':'Coding with Python'}"""


async def example_with_context_manager():
    """Using the client with context manager"""
    async with Crawl4AICloudClient(api_key="709b1fd08b8dd357fed4") as client:

        try:
            # Basic scraping
            response = await client.basic_scrape(
                url=url
            )
            print(response)

            # LLM extraction
            llm_result = await client.llm_extract(
                url=url,
                llm_instruction=llm_instruction,
                cache_mode="bypass",
            )
            print(llm_result.extractions)

        except (ScrapingError, ApiError) as e:
            print(f"Scraping failed: {e}")


async def example_without_context_manager():
    """Using the client without context manager"""
    client = Crawl4AICloudClient(api_key="709b1fd08b8dd357fed4")

    try:
        await client.connect()

        # Basic scraping
        response = await client.basic_scrape(
            url=url
        )
        print(response)

        # LLM extraction
        llm_result = await client.llm_extract(
            url=url,
            llm_instruction="Extract the course names",
            cache_mode="bypass",
        )
        print(llm_result.extractions)

    except (ScrapingError, ApiError) as e:
        print(f"Scraping failed: {e}")
    finally:
        await client.close()


# Run examples
async def main():
    print("Running with context manager:")
    await example_with_context_manager()

    print("\nRunning without context manager:")
    await example_without_context_manager()


if __name__ == "__main__":
    asyncio.run(main())
```

### Error Handling

All methods may raise `ScrapingError` or `ApiError`. Always use try-except blocks:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient, ScrapingError, ApiError

async def main():
  async with Crawl4AICloudClient(api_key="your_api_key") as client:
      try:
          response = await client.basic_scrape(
              url="https://www.kidocode.com/degrees/technology"
          )
          print(response)
      except (ScrapingError, ApiError) as e:
          print(f"Scraping failed: {e}")

asyncio.run(main())
```

## Examples from official API docs using library:

- [Quickstart Guides](#quickstart-guides)
  - [Basic Scraping](#quickstart-1-basic-scraping-that-turns-a-webpage-into-markdown) (🦾more robust)
  - [LLM-based Extraction](#quickstart-2-scrape--extract-with-llm-based-extraction) (⚡lower latency)
  - [JSON CSS-based Extraction](#quickstart-3-scrape--extract-with-json-css-extraction--schema)
- [List of API Parameters](#api-parameters-details--examples)
  - [Output Format](#output-format-options)
  - [Page Interaction & JS Execution](#page-interaction--js-code-execution)
  - [Magic Mode](#magic-mode)
  - [iFrame Processing](#processing-iframes)
  - [Overlay Removal](#removing-overlay-elements)
  - [HTML Tag Exclusion](#excluding-html-tags)
  - [Waiting for DOM Element](#waiting-for-dom-element-to-load)
  - [CSS Selector](#css-selector-targeting)
  - [Word Count Threshold](#word-count-threshold)
  - [Screenshot Capture](#screenshot-capture)
  - [Cache Control](#cache-control)
  - [LLM Instruction & Schema](#llm-instruction-and-schema)
  - [JSON CSS Extraction](#json-css-based-extraction)
  - [Schema Generator Utility](#utilityhelper-api-css-schema-generator)

## Quickstart Guides

### Quickstart #1: Basic Scraping that Turns a Webpage into Markdown

**Simple scraping without extraction costs 1 API credit per API call.**

Basic scraping that ingests an URL and outputs markdown content and other essential information such as page metadata, multimedia content, links, etc.

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url="https://www.kidocode.com/degrees/technology"
        )
        print(response)
asyncio.run(main())
```

### Quickstart #2: Scrape + Extract with LLM-based Extraction

**Scraping + extraction costs 2 API credits per API call**

Scrape + extract with LLM-based extraction logic. 🦾Recommended for use cases that require reliable extraction results but the underlying webpage structure frequently and unpredictably changes

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

# Define schema for structured extraction
llm_schema = {
    "course_name": "name of the course offered",
}

# Instruction for LLM extraction
llm_instruction = """Extract the course name of each item listed in the "Explore our future-forward courses" section.
The extraction should look like: {'course_name':'Coding with Python'}"""

async def main():
    # Make request to public API
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.llm_extract(
            url="https://www.kidocode.com/degrees/technology",
            llm_instruction=llm_instruction,
            llm_schema=llm_schema,
            cache_mode="bypass"
        )
        print(response.extractions)

asyncio.run(main())

```

### Quickstart #3: Scrape + Extract with JSON CSS Extraction & Schema

**Scraping + extraction costs 2 API credits per API call**

Extract structured data from web pages using CSS selectors and optional JavaScript pre-processing, with no LLM needed. ⚡Recommended for use cases that value fast extraction on mostly static webpage structures. 

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

# JavaScript to execute before extraction
js_code = """
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
"""

# Define extraction schema using CSS selectors
json_css_schema = {
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
            "attribute": "src"
        }
    ]
}

async def main():
    # Make API request
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.json_css_extract(
            url=url,
            json_css_schema=json_css_schema,
            js_code=js_code,
            cache_mode="bypass"
        )
        print(response.extractions)

asyncio.run(main())

```

## API Parameters: Details & Examples

### Output Format Options

Control the format of the crawled content using the output_format parameter. Review detailed documentation on the 4 output options: html, cleaned_html, markdown, fit_markdown.

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    # Make API request with output format
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            output_format="html"  # Options: html, cleaned_html, markdown, fit_markdown
        )
        print(response)

asyncio.run(main())

```

### Page Interaction & JS Code Execution

Execute custom JavaScript code on the target page before extraction

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

# JavaScript code to execute on the page
js_code = """
window.scrollTo(0, document.body.scrollHeight);
document.querySelector('#fr-submit-btn').click();
"""

async def main():
    # Make API request with output format
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url="https://www.kidocode.com/franchise",
            js_code=js_code,
            cache_mode="bypass" 
        )
        print(response)

asyncio.run(main())
```
#### JavaScript Code Features:

    ✓ Execute custom JavaScript on target page
    ✓ Interact with page elements (click, scroll, etc.)
    ✓ Modify page content before extraction
    ✓ Wait for dynamic content to load

Perfect for interactive pages that require user actions before content is available


### Magic Mode

Enable comprehensive anti-bot protection bypass with the magic parameter. [Review detailed documentation.](https://crawl4ai.com/mkdocs/advanced/identity-based-crawling/#4-magic-mode-simplified-automation)

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            magic=True
        )
        print(response)

asyncio.run(main())

```
#### Magic Mode Features:

    ✓ Masks browser automation signals
    ✓ Simulates human-like behavior
    ✓ Handles cookie consent popups
    ✓ Manages browser fingerprinting


### Processing iFrames

Enable crawling of content within iframes:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            process_iframes=True
        )
        print(response)

asyncio.run(main())
```
#### iFrame Processing:
    ✓ Crawls content within embedded iframes
    ✓ Disabled by default for faster crawling
    ✓ Useful for sites with embedded content
    ✓ May increase total crawl time


### Removing Overlay Elements

Remove popups, ads, and other overlay elements during crawling:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            remove_overlay_elements=True
        )
        print(response)

asyncio.run(main())

```
#### Overlay Removal Features:
    ✓ Removes advertisement overlays
    ✓ Clears cookie consent notices
    ✓ Eliminates modal popups
    ✓ Improves content extraction



### Excluding HTML Tags

Filter out specific HTML elements during content extraction:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            excluded_tags=["nav", "form"]  # Ignore navigation and forms
        )
        print(response)

asyncio.run(main())

```
#### Tag Exclusion Features:
    ✓ Filter out irrelevant HTML elements
    ✓ Focus extraction on main content
    ✓ Customize content processing
    ✓ Default: process all tags (empty list)


### Waiting for DOM Element to Load

Specify elements to wait for before processing the page:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = 'https://www.kidocode.com/degrees/technology'

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            wait_for="css:.dynamic-content"
        )
        print(response)

asyncio.run(main())
```
#### Wait For Features:
    ✓ Wait for AJAX-loaded content
    ✓ Support for CSS and XPath selectors
    ✓ Ensures complete page loading
    ✓ Perfect for dynamic web apps
_Format: Use "css:.selector" for CSS selectors or "xpath://div" for XPath expressions_


### CSS Selector Targeting

Focus content extraction on specific page elements:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            css_selector=".margin-bottom-24px"  # Only process matching elements
        )
        print(response)

asyncio.run(main())

```
#### CSS Selector Features:
    ✓ Target specific page elements
    ✓ Extract only relevant content
    ✓ Reduce processing overhead
    ✓ Improve extraction accuracy
_Use standard CSS selector syntax to identify target elements_


### Word Count Threshold

Filter content blocks based on minimum word count:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            word_count_threshold=10
        )
        print(response)

asyncio.run(main())
```
#### Word Count Features:
    ✓ Filter out short text snippets
    ✓ Focus on substantial content
    ✓ Improve extraction quality
    ✓ Reduce noise in results
_Set threshold based on your content requirements_

### Screenshot Capture

Take screenshots of web pages with optional delay:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient, decode_base64

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            screenshot=True,
            screenshot_wait_for=2.0
        )
        print(response)

    # Save screenshot to file if available
    if response.screenshot != "DISABLED":
        with open("screenshot.png", "wb") as f:
            f.write(decode_base64(response.screenshot))

asyncio.run(main())
```
#### Screenshot Features:
    ✓ Capture full page screenshots
    ✓ Optional delay before capture
    ✓ Returns base64 encoded PNG
    ✓ Perfect for visual verification
_Use screenshot_wait_for parameter to ensure dynamic content is loaded_

**Note: Due to payload size and latency considerations, LLM extraction and JSON-CSS extraction will be disabled when screenshot is enabled.**

### Cache Control

Control caching behavior for content retrieval:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.basic_scrape(
            url=url,
            cache_mode="bypass"  # Always fetch fresh content
        )
        print(response)

asyncio.run(main())
```
#### Cache Control Features:
- ✓ Default caching enabled for performance
- ✓ Optional bypass for fresh content
- ✓ Trade-off between speed and freshness
- ✓ Useful for frequently updated content
_Note: Using cache bypass may increase response times_


### LLM Instruction and Schema

Extract structured data using LLM instructions and optional schema definitions:

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

# Define schema for structured extraction
llm_schema = {
    "course_name": "name of the course offering",
    "course_description": "description of the course offering",
}

# Instruction for LLM extraction
llm_instruction = "Extract the course_name and course_description of each course."

async def main():
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.llm_extract(
            url=url,
            llm_instruction=llm_instruction,
            llm_schema=llm_schema,
            input_format="markdown",  # valid values are markdown (default), fit_markdown, and html
            cache_mode="bypass"  # Always fetch fresh content
        )
        print(response)

asyncio.run(main())
```

#### LLM Parameters:

**llm_instruction** - Natural language prompt for extraction (max 200 tokens)

**llm_schema** - Optional dictionary defining expected fields and their descriptions
    
**input_format** - Optional parameter that specified which page content is fed to the LLM for extraction. By default, input_format is set to "markdown", meaning the page's markdown is fed to the LLM. You can also set the parameter to "fit_markdown" or "html". The "fit_markdown" setting in particular can drastically reduce the number of tokens sent to LLMs (if you trust the underlying markdown filtering logic).

_Note: If no schema is provided, the LLM will infer the structure from the instruction._


### JSON CSS based Extraction

The JSON-CSS-based extraction is a powerful feature of Crawl4AI that allows you to extract structured data from web pages using CSS selectors. This method is particularly useful when you need to extract specific data points from a consistent HTML structure, such as tables or repeated elements. Here's how to use it with the AsyncWebCrawler. All you need is to define a schema that specifies: 1. A base CSS selector for the repeating elements 2. Fields to extract from each element, each with its own CSS selector. This strategy is fast and efficient, as it doesn't rely on external services like LLMs for extraction.

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient

url = "https://www.kidocode.com/degrees/technology"

# Define extraction schema using CSS selectors
llm_instruction = "Extract the course_name and course_description of each course."

# Define extraction schema using CSS selectors
json_css_schema = {
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
            "attribute": "src"
        }
    ]
}

async def main():
    # Make API request
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.json_css_extract(
            url=url,
            json_css_schema=json_css_schema,
            cache_mode="bypass"
        )
        print(response.extractions)

asyncio.run(main())
```

### Utility/Helper API: CSS Schema Generator

Don't want to manually create JSON CSS schema? You can use this utility/helper API to turn raw HTML content into the corresponding JSON CSS schema.

```python
import asyncio
from crawl4aicloud import Crawl4AICloudClient


html = """
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

async def main():
    # Make API request
    async with Crawl4AICloudClient(api_key="your_api_key") as client:
        response = await client.json_css_schema_generator(
            html=html
        )
        print(response)

asyncio.run(main())
```
