import scrapy
from wizardoflegend.items import Arcana
import stringcase


class ArcanaSpider(scrapy.Spider):
    name = "arcanas"
    start_urls = [
        'https://wizardoflegend.gamepedia.com/Arcana'
    ]


    def parse(self, response):
        table = response.css('table.wikitable.cargo-arcana-table')
        rows = table.css('tbody tr')
        # removing the first one since its the header
        del(rows[0])

        for row in rows:
            relic = Arcana()
            relic['item_name'] = 'arcana'
            print(row.css('td:nth-child(2) a').xpath('@title').get())
            relic['id'] = stringcase.snakecase(stringcase.alphanumcase(row.css('td:nth-child(2) a').xpath('@title').get()))
            relic['image_urls'] = [row.css('td:nth-child(1) a img').xpath('@src').get()]
            relic['name'] = row.css('td:nth-child(2) a').xpath('@title').get()
            relic['description'] = row.css('td:nth-child(3)').xpath('text()').get()
            relic['element'] = row.css('td:nth-child(4) a').xpath('@title').get()
            relic['type'] = row.css('td:nth-child(5)').xpath('text()').get()
            relic['damage'] = row.css('td:nth-child(6)').xpath('text()').get()
            relic['cooldown'] = row.css('td:nth-child(7)').xpath('text()').get()
            relic['knockback'] = row.css('td:nth-child(8)').xpath('text()').get()
            relic['duration'] = row.css('td:nth-child(9)').xpath('text()').get()
            relic['cost_gems'] = row.css('td:nth-child(10)').xpath('text()').getall()[0].strip() or 'N/A'
            relic['cost_coins'] = row.css('td:nth-child(10)').xpath('text()').getall()[1].strip() or 'N/A'
            relic['pool'] = row.css('td:nth-child(11)').xpath('text()').get() or 'N/A'
            yield relic
