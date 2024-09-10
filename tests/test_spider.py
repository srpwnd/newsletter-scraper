import unittest

from scrapy.http import HtmlResponse

from scraping_pipeline import BizztreatSpider


class TestBizztreatSpider(unittest.TestCase):
    def setUp(self):
        self.spider = BizztreatSpider()

    def test_parse(self):
        # Define a mock HTML response
        html = """
        <html>
            <body>
                <div class="entry">
                    <h3 class="entry-title"><a title="Test Title" href="http://example.com/test-url">Test Title</a></h3>
                    <div class="entry-meta-published"><span class="entry-meta-value">2024-01-01</span></div>
                    <div class="entry-meta-articles_author"><span class="entry-meta-value">John Doe</span></div>
                    <a class="image" href="http://example.com/test-img.jpg"></a>
                </div>
                <li class="pagination-next"><a href="http://example.com/next-page"></a></li>
            </body>
        </html>
        """

        # Mock a Scrapy HtmlResponse object
        response = HtmlResponse(url="http://example.com", body=html, encoding="utf-8")

        # Call parse method and get the result
        results = list(self.spider.parse(response))

        # Test the pagination (next page)
        next_page = results[0]
        self.assertEqual(next_page.url, "http://example.com/next-page")

        # Test the extracted post data
        post = results[1]
        expected_post = {
            "newsletter": {
                "title": "Test Title",
                "date": "2024-01-01",
                "author": "John Doe",
                "url": "http://example.com/test-url",
                "img_url": "http://example.com/test-img.jpg",
            }
        }
        self.assertEqual(post, expected_post)


if __name__ == "__main__":
    unittest.main()
