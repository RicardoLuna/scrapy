# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KabumItem(scrapy.Item):
    nome = scrapy.Field()
    url_imagens = scrapy.Field()
    url_produto = scrapy.Field()
    preco_normal = scrapy.Field()
    preco_desc = scrapy.Field()
    categoria = scrapy.Field()
    sub_categorias = scrapy.Field()
