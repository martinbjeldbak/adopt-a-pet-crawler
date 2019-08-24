# -*- coding: utf-8 -*-
import scrapy
import json

class CatsSpider(scrapy.Spider):
    name = 'cats'
    allowed_domains = ['adoptapet.com.au']
    start_urls = ['http://adoptapet.com.au/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                                                url='https://www.adoptapet.com.au/search',
                                                formdata={'state': '1',
                                                          'location': '0',
                                                          'animal_type': 'custom-mapping-2',
                                                          'breed': '0',
                                                          'colour': '0',
                                                          'sex': '0'},
                                                callback=self.after_search
                                                )
    def after_search(self, response):
        pattern = r'\bvar\s+init_animals\s*=\s*(\[\{.*?\}\])\s*;\s*\n'
        animal_json_data = response.xpath('/html/body/script[17]/text()').re_first(pattern)
        animals = json.loads(animal_json_data)
        scrapy.utils.response.open_in_browser(response)
        from scrapy.shell import inspect_response
        inspect_response(response, self)
