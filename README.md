# scrapy
### Teste prático de Scraping.
### Target: [https://www.kabum.com.br/]

### Objetivos 
- Construir um crawler para alguma loja online utilizando o framework Scrapy.
- Utilização de xpath nas buscas por links (Ok!)
- Persistência das informações (Ok!)
  - MongoDB(Testado)
- Utilizar logs para sinalizar ocorrências durante o scraping - Quando os dados são armazenados - (Ok!)

### Comandos para instalar as bibliotecas
- pip install scrapy
- pip install pymongo

### Comando para o projeto
- scrapy startproject nome_projeto (cria o projeto)
- scrapy genspider nome_spider url_site (cria o spider)
- scrapy crawl nome_spider (inicia o spider(nome_spider) do projeto )

### Campos
- nome , url_produto, url_imagens, preco_normal, preco_desc, categoria, sub_categorias


### Visualização do dados
- Instalar o [Mongodb](https://www.mongodb.com/) 
- Usar o comando mongod utilizando o prompt para iniciar o servidor. 
- E para visualização foi utilizado o [Robo 3T](https://robomongo.org/).


### Spider
- parse:
  - Gera o link que acessar a categoria
  - Dentro de categorias faz a chamada para próxima pagina dos itens
- parse_next:
    - Inicialmente extrai os itens
    - Pega os links para as outras páginas de itens   
- parse_item:
    - Faz as requisição para os itens usando o link do produto   
- parse_produto:
  - Extrai os dados do produto    
    
 ### Programa feito em 5h 
 ### Resolvendo problemas 2h 
 ### Estudando [10 h]
 
 ### Referências:
 - [WEB SCRAPING COM SCRAPY](https://pythonhelp.wordpress.com/2014/08/05/web-scraping-com-scrapy-primeiros-passos/)
 - [Scrapy](http://trumae.blogspot.com.br/2014/01/scrapy-bem-facinho.html)
 - [Settings scrapy](https://doc.scrapy.org/en/latest/topics/settings.html#settings)
 - [Python Driver (PyMongo)](https://docs.mongodb.com/getting-started/python/client/)
 - [This tutorial is intended as an introduction to working with MongoDB and PyMongo.](http://api.mongodb.com/python/current/tutorial.html)
 - [Web Scraping With Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
 - [Web Scraping and Crawling With Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-and-crawling-with-scrapy-and-mongodb/)
 - [Scrapy 1.4 documentation](https://doc.scrapy.org/en/latest/)
 
 
