# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
class PicItem (Item):
#    title=Field()
    url=Field()
 #   infobox=Field()
    gericht=Field()
    datum=Field()
    AZ= Field()
    typ= Field()
    text=Field()
    verfahrensgang=Field()


    rechtsgebiete= Field()

