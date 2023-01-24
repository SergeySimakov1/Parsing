import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ParserJobItem

class HhRuSpider(scrapy.Spider):
    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://krasnodar.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&excluded_text=&area=53&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20'
       ]

    def parse(self, response: HtmlResponse):

        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vacancies_links = response.xpath("//a[@data-qa='serp-item__title']/@href").getall()
        for link in vacancies_links:
            yield response.follow(link, callback=self.parse_vacancy)

    def parse_vacancy(self, response: HtmlResponse):

        vacancies_name = response.css('h1::text').get()
        vacancies_url = response.url
        vacancies_salary = response.xpath('//div[@data-qa="vacancy-salary"]//text()').getall()

        yield ParserJobItem (
            name = vacancies_name,
            url = vacancies_url,
            salary = vacancies_salary
        )
