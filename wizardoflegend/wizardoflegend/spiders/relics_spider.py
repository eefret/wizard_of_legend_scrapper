import scrapy
from wizardoflegend.items import Relic
import stringcase


class RelicsSpider(scrapy.Spider):
    name = "relics"
    start_urls = [
        'https://wizardoflegend.gamepedia.com/Relics'
    ]


    def parse(self, response):
        table = response.css('.wikitable')
        rows = table.css('tbody tr')
        # removing the first one since its the header
        del(rows[0])

        for row in rows:
            relic = Relic()
            relic['item_name'] = 'relic'
            relic['id'] = stringcase.snakecase(stringcase.alphanumcase(row.css('td:nth-child(2) a').xpath('@title').get()))
            relic['image_urls'] = [row.css('td:nth-child(1) a img').xpath('@src').get()]
            relic['name'] = row.css('td:nth-child(2) a').xpath('@title').get()
            relic['description'] = row.css('td:nth-child(3)').xpath('text()').get()
            relic['type'] = row.css('td:nth-child(4)').xpath('text()').get()
            relic['cost_gems'] = row.css('td:nth-child(5)').xpath('text()').getall()[0].strip()
            relic['cost_coins'] = row.css('td:nth-child(5)').xpath('text()').getall()[1].strip() or 'N/A'
            relic['pool'] = row.css('td:nth-child(6)').xpath('text()').get() or 'N/A'
            yield relic
