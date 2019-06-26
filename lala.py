# -*- coding: utf-8 -*-
import scrapy
from sectorial.items import noticia

class LalaSpider(scrapy.Spider):
    name = 'lala'

    start_urls = ['https://www.larepublica.co/economia',
                  'https://www.larepublica.co/agro',
                  'https://www.larepublica.co/finanzas',
                  'https://www.larepublica.co/empresas',
                  'https://www.larepublica.co/empresas',
                  'https://www.larepublica.co/consumo',
                  'https://www.larepublica.co/infraestructura']

    def parse(self, response):
        for href in response.css('.headline a::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback = self.parse_dir)
            
    def parse_dir(self,response):
        item = noticia() 
        item['entradilla'] = response.css('.headline a::text').get()
        item['link'] = response.url
        item['titulo'] = response.css('.lead p::text').getall()
        item['fuente'] = "La Republica"
        
        return item 
