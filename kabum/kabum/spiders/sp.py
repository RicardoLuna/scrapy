# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
import  re


class SpSpider(scrapy.Spider):
    name = 'sp'
    #allowed_domains = ['https://www.nagem.com.br/']
    start_urls = ['https://www.kabum.com.br/']

    def parse(self, response):

        #gera o link que acessa a categoria
        pag_categoria = response.xpath("//div[contains(@class, 'texto_categoria')]//@href")

        #outras paginas //*[@id="BlocoConteudo"]/div[2]/div/div[33]/form/table/tbody/tr/td[6]/span//@href
        #dentro de categorias chama a próxima pagina dos intens
        for item_cat in pag_categoria:
            #fazer a requisição para cada categoria
            p_link = item_cat.extract()
            yield scrapy.Request(
                p_link,
                callback=self.parse_next
            )
            '''

            acesso_itens = item_cat.xpath('.//div[contains(@id,"divlistaprodutos")]'
            )
            p_link = acesso_itens.xpath(
                './/div[contains(@id,"prodList_1")]//@href'
            )
            # muito util para testes

            yield scrapy.Request(
                url=response.urljoin(p_link),
                callback=self.parse_detalhes
            )
            '''


    def parse_next(self,response):
        #extair itens
        #link para as outras paginas
        link_parcial = response.xpath('.//div[contains(@class,"listagem-paginacao")]//@href')

        #armazena o link para todos os itens da pagina
        temp = response.xpath('.//div[contains(@class,"listagem-img")]//@href')

        # response.xpath('.//div[contains(@class,"content_tab")]/p')

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
        #na pagina de itens faz as requi para os itens

        temp = response.xpath('.//div[contains(@class,"listagem-img")]//@href')

        #response.xpath('.//div[contains(@class,"content_tab")]/p')

        for x in temp:
            # link para o produto
            yield scrapy.Request(
                x.extract(),
                callback=self.parse_produto
            )



    def parse_produto(self,response):

        item = {}
        #nome
        nome = response.xpath('.//div[contains(@id,"titulo_det")]').xpath('string(.)').extract_first()

        #imagens
        url_imagens = response.xpath('.//ul[contains(@id,"slide")]/li/img//@src').extract()
        #response.xpath('.//div[contains(@class,"content_tab")/p]').extract()

        #preco antigo precisa tratar
        preco_antigo = response.xpath('.//div[contains(@class,"preco_normal")]').xpath('string(.)').extract_first()


        if len(preco_antigo.split(" ")) == 10:
            #preco produto sem promocao
            preco_antigo = re.sub('\s+', '', preco_antigo)
            preco_antigo = preco_antigo.strip("R$")
            #preco_antigo = float(preco_antigo)
        else:
            #preco produto em promocao
            preco_antigo = preco_antigo.split(" ")
            #preco_antigo = float(preco_antigo[1])


        #preco atual
        preco_desc = response.xpath('.//span[contains(@class,"preco_desconto")]').xpath('string(.)').extract_first()

        preco_desc = preco_desc.split(" ")

        if len(preco_desc) > 14:
            preco_desc = preco_desc[14]
            #preco_desc = preco_desc.replace(',', '.')
            #preco_desc = float(preco_desc)

        else:
            preco_desc = preco_desc[1]
            #preco_desc = float(preco_desc)


        #url
        url_produto = response.url

        #lista caract
        #lista_caract = response.xpath('.//div[contains(@class,"content_tab")]/p').xpath('string(.)').extract()
        #marca = lista_caract[9].split(" ")[2]

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

