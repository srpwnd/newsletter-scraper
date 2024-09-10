from typing import Any

import dlt
from scrapy import Spider  # type: ignore
from scrapy.http import Response  # type: ignore

from scraping import run_pipeline


class BizztreatSpider(Spider):
    name = "bizztreat"

    def parse(self, response: Response, **kwargs: Any) -> Any:
        for next_page in response.css("li.pagination-next a::attr(href)"):
            if next_page:
                yield response.follow(next_page, self.parse)

        for post in response.css("div.entry"):
            result = {
                "newsletter": {
                    "title": post.css("h3.entry-title a::attr(title)").get(),
                    "date": post.css("div.entry-meta-published span.entry-meta-value::text").get(),
                    "author": post.css(
                        "div.entry-meta-articles_author span.entry-meta-value::text"
                    ).get(),
                    "url": post.css("h3.entry-title a::attr(href)").get(),
                    "img_url": post.css("a.image::attr(href)").get(),
                },
            }
            yield result


def scrape_posts_csv() -> None:
    """Scrape posts and save them to a CSV file"""

    pipeline = dlt.pipeline(
        pipeline_name="scraping",
        destination="filesystem",
        dataset_name="posts_csv",
    )

    run_pipeline(
        pipeline,
        BizztreatSpider,
        # you can pass scrapy settings overrides here
        scrapy_settings={
            "DEPTH_LIMIT": 100,
        },
        write_disposition="append",
        loader_file_format="csv",
    )


def scrape_posts_parquet() -> None:
    """Scrape posts and save them to a Parquet file"""

    pipeline = dlt.pipeline(
        pipeline_name="scraping",
        destination="filesystem",
        dataset_name="posts_parquet",
    )

    run_pipeline(
        pipeline,
        BizztreatSpider,
        # you can pass scrapy settings overrides here
        scrapy_settings={
            "DEPTH_LIMIT": 100,
        },
        write_disposition="append",
        loader_file_format="parquet",
    )


if __name__ == "__main__":
    scrape_posts_csv()
    # scrape_posts_parquet()
