# -*- coding: utf-8 -*-
import scrapy
import json
from adoptapet.items import Pet

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
        raw_animals = json.loads(animal_json_data)

        animals = []
        for raw_animal in raw_animals:
            animals.append(Pet(
                id=raw_animal['id']
                adoption_cost=raw_animal['adoptionCost']
                created_at=raw_animal['created_at']
                updated_at=raw_animal['updated_at']
                description=raw_animal['description1']
                date_of_birth=raw_animal['date_of_birth']
                is_desexed=raw_animal['isDesexed']
                sex=raw_animal['sex']))

        return animals
