# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose

def process_price(value):
    money = 0
    currency = ''
    if value:
        money = int(value[0].replace(' ',''))
        currency = value[1]
    return {'money': money, 'currency': currency}

# def name_site_add(links):
#     if links:
#         mod_links = []
#         for i in range(len(links)):
#             mod_links.append('https://www.castorama.ru' + links[i].get())
#     return mod_links


class CastoramaParserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price), output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())