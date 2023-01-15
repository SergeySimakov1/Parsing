# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from pymongo import MongoClient

class ParserJobPipeline:

    def __init__(self):

        client = MongoClient('localhost:27017')
        self.mongo_db = client.parser_5ka


    def process_item(self, item, spider):

        price = ''

        # переводим в число полученные цены в строковом виде с  пробелами и записываем в БД уже цену в виде числа
        for el in item['cost']:
            if el.isdigit():
                price += el
        item['cost'] = int(price)

        collection = self.mongo_db[spider.name]
        collection.insert_one(item)

        return item
