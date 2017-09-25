# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
import re


class SpSpider(scrapy.Spider):
    name = 'sp'
    start_urls = ['https://www.kabum.com.br/']

    def parse(self, response):

        pag_categoria = response.xpath("//div[contains(@class, 'texto_categoria')]//@href")

        for item_cat in pag_categoria:
            #fazer a requisição para cada categoria
            p_link = item_cat.extract()
            yield scrapy.Request(
                p_link,
                callback=self.parse_next
            )


    def parse_next(self,response):

        link_parcial = response.xpath('.//div[contains(@class,"listagem-paginacao")]//@href')

        temp = response.xpath('.//div[contains(@class,"listagem-img")]//@href')

        for x in temp:
            # link para o produto
            yield scrapy.Request(
                x.extract(),
                callback=self.parse_produto
            )


        if len(link_parcial) > 0:
            for link in link_parcial:
                yield scrapy.Request(
                    url=response.urljoin(link.extract()),
                    callback=self.parse_item
                )

    def parse_item(self,response):

        temp = response.xpath('.//div[contains(@class,"listagem-img")]//@href')

        for x in temp:
            # link para o produto
            yield scrapy.Request(
                x.extract(),
                callback=self.parse_produto
            )



    def parse_produto(self,response):

        item = {}
        nome = response.xpath('.//div[contains(@id,"titulo_det")]').xpath('string(.)').extract_first()
        url_imagens = response.xpath('.//ul[contains(@id,"slide")]/li/img//@src').extract()

        preco_antigo = response.xpath('.//div[contains(@class,"preco_normal")]').xpath('string(.)').extract_first()

        if len(preco_antigo.split(" ")) == 10:

            preco_antigo = re.sub('\s+', '', preco_antigo)
            preco_antigo = preco_antigo.strip("R$")

        else:
            preco_antigo = preco_antigo.split(" ")[1]


        #preco atual
        preco_desc = response.xpath('.//span[contains(@class,"preco_desconto")]').xpath('string(.)').extract_first()

        preco_desc = preco_desc.split(" ")

        if len(preco_desc) > 14:
            preco_desc = preco_desc[14]

        else:
            preco_desc = preco_desc[1]


        #url
        url_produto = response.url

        #categoria
        temp = response.xpath('.//div[contains(@class,"links_det")]//@href').extract()
        categoria = temp[0].split("/")[3]

        sub_categorias = []

        sub_categorias.append(temp[3].split("/")[3])
        sub_categorias.append(temp[3].split("/")[4])
        sub_categorias.append(temp[3].split("/")[5])

        item['nome'] = nome
        item['url_imagens'] = url_imagens
        item['url_produto'] = url_produto
        item['preco_normal'] = preco_antigo
        item['preco_desc'] = preco_desc
        item['categoria'] = categoria
        item['sub_categorias'] = sub_categorias
        yield item

