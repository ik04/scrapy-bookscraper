import scrapy
from bookscraper.items import CategoryItem


class CategoryspiderSpider(scrapy.Spider):
    name = "categoryspider"
    custom_settings = {
        "ITEM_PIPELINES": {
            "bookscraper.pipelines.CategoryScraperPipeline": 400,
        },
        "FEEDS": {
            "categories.json": {"format": "json"},
        },
    }
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        categories = response.xpath(
            "/html/body/div[1]/div/div/aside/div[2]/ul/li/ul/li"
        )
        for category in categories:
            name = category.css("a ::text").get()
            name = name.strip()
            category_item = CategoryItem()
            category_item["category"] = name
            yield category_item
