import unittest
from unittest.mock import patch

from scraping_pipeline import BizztreatSpider, scrape_posts_csv, scrape_posts_parquet


class TestPipelineIntegration(unittest.TestCase):
    @patch("scraping_pipeline.run_pipeline")
    def test_scrape_posts_csv(self, mock_run_pipeline):
        # Mock the pipeline method
        mock_run_pipeline.return_value = None

        # Run the function
        scrape_posts_csv()

        # Assert that run_pipeline was called with BizztreatSpider and correct settings
        mock_run_pipeline.assert_called_once()
        args, kwargs = mock_run_pipeline.call_args

        # Ensure that the second argument is the BizztreatSpider class
        self.assertEqual(args[1], BizztreatSpider)

        # Check if scrapy_settings and loader_file_format are set correctly
        self.assertEqual(kwargs["scrapy_settings"], {"DEPTH_LIMIT": 100})
        self.assertEqual(kwargs["loader_file_format"], "csv")

    @patch("scraping_pipeline.run_pipeline")
    def test_scrape_posts_parquet(self, mock_run_pipeline):
        # Mock the pipeline method
        mock_run_pipeline.return_value = None

        # Run the function
        scrape_posts_parquet()

        # Assert that run_pipeline was called with BizztreatSpider and correct settings
        mock_run_pipeline.assert_called_once()
        args, kwargs = mock_run_pipeline.call_args

        # Ensure that the second argument is the BizztreatSpider class
        self.assertEqual(args[1], BizztreatSpider)

        # Check if scrapy_settings and loader_file_format are set correctly
        self.assertEqual(kwargs["scrapy_settings"], {"DEPTH_LIMIT": 100})
        self.assertEqual(kwargs["loader_file_format"], "parquet")


if __name__ == "__main__":
    unittest.main()
