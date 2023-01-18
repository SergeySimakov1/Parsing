import scrapy
from scrapy.http import HtmlResponse
from castorama_parser.items import CastoramaParserItem
from scrapy.loader import ItemLoader

class CastoramaSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://www.castorama.ru/catalogsearch/result/?q={kwargs.get("search")}']


    def parse(self, response: HtmlResponse):

        links = response.xpath("//a[@class='product-card__img-link']")
        for link in links:
            yield response.follow(link, callback=self.parse_castorama)

    def parse_castorama(self, response: HtmlResponse):
        print()
        loader = ItemLoader(item=CastoramaParserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@class='price']/span/span/text()")
        loader.add_xpath('photos', "//span[@itemprop='image']/@content")
        loader.add_value('url', response.url)
        yield loader.load_item()

        # name = response.xpath("//h1/text()").get()
        # price = response.xpath("//h3//text()").getall()
        # photos = response.xpath("//div[@class='swiper-zoom-container']/img/@src | //div[@class='swiper-zoom-container']/img/@data-src").getall()
        # url = response.url
        # yield CastoramaParserItem(name=name, price=price, photos=photos, url=url)