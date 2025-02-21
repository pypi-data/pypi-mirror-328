import asyncio
import os
import sys
import pytest
from unittest.mock import AsyncMock, patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crawk import crawl_and_save, crawl_url, save_markdown

@pytest.mark.asyncio
async def test_crawl_and_save():
    with patch("crawk.crawl_url") as mock_crawl_url:
        mock_crawl_url.return_value = None
        await crawl_and_save("http://example.com", max_depth=1, concurrency=1)
        mock_crawl_url.assert_called_once()

@pytest.mark.asyncio
async def test_crawl_url():
    mock_crawler = AsyncMock()
    mock_crawler.arun.return_value = AsyncMock(
        markdown="test markdown",
        links={"internal": []}
    )
    with patch("crawk.save_markdown") as mock_save_markdown:
        await crawl_url(mock_crawler, "http://example.com", 0, "example.com", set(), [])
        mock_save_markdown.assert_called_once()

def test_save_markdown(tmpdir):
    url = "http://example.com/test"
    content = "test content"
    save_markdown(url, content)
    
    domain = "example.com"
    path = "test"
    
    expected_path = os.path.join("docs", domain, f"{path}.md")
    
    assert os.path.exists(expected_path)
    with open(expected_path, "r") as f:
        assert f.read() == content