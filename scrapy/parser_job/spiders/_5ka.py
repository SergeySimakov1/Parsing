import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ParserJobItem

class _5kaSpider(scrapy.Spider):
    name = '_5ka'
    allowed_domains = ['5ka.ru']
    start_urls = ['https://5ka.ru/special_offers']

    def parse(self, response: HtmlResponse):

        # парсим страницу с акциями на сайте "Пятерочки"

        hits_names = response.xpath("//div[@class='product-card item']//img/@alt").getall()
        hits_costs = response.xpath("//div[@class='product-card item']/div/div/span/text()").getall()

        for i, hit_name in enumerate(hits_names):
            yield ParserJobItem(
                name = hit_name,
                cost = hits_costs[i]
            )
