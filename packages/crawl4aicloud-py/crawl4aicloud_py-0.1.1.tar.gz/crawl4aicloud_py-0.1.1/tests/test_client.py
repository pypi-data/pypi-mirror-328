import pytest

from crawl4aicloud import ScrapingError
from crawl4aicloud.client import Crawl4AICloudClient
from crawl4aicloud.schemas import (
    ResultSuccess,
    ResultSchema,
    Metadata,
    JsonCssSchema,
    JsonCssField,
)

#
# Test for basic_scrape
#
DUMMY_API_KEY = "dummy-api-key1234567"


@pytest.mark.asyncio
async def test_basic_scrape_success(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        return ResultSuccess(
            content="Test content",
            links=[],
            images=[],
            videos=[],
            audios=[],
            metadata=Metadata(),
            screenshot="DISABLED",
            extractions=[],
        )

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        result = await client.basic_scrape(
            url="https://example.com", output_format="markdown"
        )
        assert isinstance(result, ResultSuccess)
        assert result.content == "Test content"


@pytest.mark.asyncio
async def test_basic_scrape_error(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        raise ScrapingError("Dummy error occurred")

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        with pytest.raises(ScrapingError) as exc_info:
            await client.basic_scrape(url="https://example.com")
        assert str(exc_info.value) == "Dummy error occurred"


#
# Test for llm_extract
#


@pytest.mark.asyncio
async def test_llm_extract_success(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        return ResultSuccess(
            content=None,
            links=[],
            images=[],
            videos=[],
            audios=[],
            metadata=Metadata(),
            screenshot="DISABLED",
            extractions=[
                {
                    "course_name": "Test Course",
                    "course_description": "Test Desc",
                    "error": False,
                }
            ],
        )

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        result = await client.llm_extract(
            url="https://example.com",
            llm_instruction="Extract course details",
            llm_schema={
                "course_name": "Course name",
                "course_description": "Course description",
            },
        )
        assert isinstance(result, ResultSuccess)
        assert result.extractions[0]["course_name"] == "Test Course"


@pytest.mark.asyncio
async def test_llm_extract_error(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        raise ScrapingError("LLM extraction failed")

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        with pytest.raises(ScrapingError) as exc_info:
            await client.llm_extract(
                url="https://example.com", llm_instruction="Extract course details"
            )
        assert str(exc_info.value) == "LLM extraction failed"


#
# Test for json_css_extract
#


@pytest.mark.asyncio
async def test_json_css_extract_success(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        return ResultSuccess(
            content="Dummy content",
            links=[],
            images=[],
            videos=[],
            audios=[],
            metadata=Metadata(),
            screenshot="DISABLED",
            extractions=[{"dummy": "value"}],
        )

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    # Construct a dummy JSON-CSS schema
    json_css_schema = JsonCssSchema(
        name="Dummy Schema",
        base_selector=".dummy",
        fields=[JsonCssField(name="dummy", selector=".dummy", type="text")],
    )

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        result = await client.json_css_extract(
            url="https://example.com",
            json_css_schema=json_css_schema,
            output_format="markdown",
        )
        assert isinstance(result, ResultSuccess)
        assert result.content == "Dummy content"
        assert isinstance(result.extractions, list)


@pytest.mark.asyncio
async def test_json_css_extract_error(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        raise ScrapingError("CSS extraction failed")

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    json_css_schema = JsonCssSchema(
        name="Dummy Schema",
        base_selector=".dummy",
        fields=[JsonCssField(name="dummy", selector=".dummy", type="text")],
    )

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        with pytest.raises(ScrapingError) as exc_info:
            await client.json_css_extract(
                url="https://example.com", json_css_schema=json_css_schema
            )
        assert str(exc_info.value) == "CSS extraction failed"


#
# Test for json_css_schema_generator
#


@pytest.mark.asyncio
async def test_json_css_schema_generator_success(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def fake_request(self, payload):
        dummy_schema = JsonCssSchema(
            name="Generated Schema",
            base_selector=".dummy",
            fields=[JsonCssField(name="test", selector=".test", type="text")],
        )
        return ResultSchema(schema=dummy_schema)

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    html_input = "<div class='dummy'><span class='test'>Test</span></div>"

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        result = await client.json_css_schema_generator(html=html_input)
        assert isinstance(result, ResultSchema)
        schema = result.model_dump(by_alias=True)["schema"]
        assert schema["name"] == "Generated Schema"
        assert schema["baseSelector"] == ".dummy"


@pytest.mark.asyncio
async def test_json_css_schema_generator_error(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_request(self, payload):
        raise ScrapingError("Schema generation failed")

    monkeypatch.setattr(Crawl4AICloudClient, "_request", fake_request)

    html_input = "<div class='dummy'><span class='test'>Test</span></div>"

    async with Crawl4AICloudClient(api_key=DUMMY_API_KEY) as client:
        with pytest.raises(ScrapingError) as exc_info:
            await client.json_css_schema_generator(html=html_input)
        assert str(exc_info.value) == "Schema generation failed"
