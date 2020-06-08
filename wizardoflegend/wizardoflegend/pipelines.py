# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ImageDownloaderPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        return '%s/%s.png' % (request.meta['type'], request.meta['image_name'])
    
    def get_media_requests(self, item, info):
        yield Request(item['image_urls'][0], meta={'image_name': item['id'], 'type': item['item_name']})
