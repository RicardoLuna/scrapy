# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem

import logging

logger = logging.getLogger(__name__)


class KabumPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Item Inválido {0}!".format(data))
        if valid:
            if item.get('nome') in self.collection.distinct('nome') \
                    and item.get('url_produto', '') in self.collection.distinct('url_produto'):
                raise DropItem("Item Duplicado {0}".format(item['nome']))

            elif item.get('url_produto', '') in self.collection.distinct('url_produto'):
                logger.info("Produto adicionado no banco de dados MongoDB!")
                self.collection.insert(dict(item))

            elif not item.get('nome') in self.collection.distinct('nome'):
                logger.info("Produto adicionado no banco de dados MongoDB!")
                self.collection.insert(dict(item))

        return item

