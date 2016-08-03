# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from Crawling.items import PicItem



class RedditSpider(CrawlSpider):
    name = "reddit"
    allowed_domains = ["openjur.de"]
    start_urls = (
        'http://openjur.de/u.html',
    )
    rules = [
        Rule(LinkExtractor(allow=["\/u\/[0-9]+\.html"]),

                callback="parse_item"



             ),
        Rule(LinkExtractor(allow=["\/u(\-[0-9]+)?\.html"])



            )
    ]
    def parse_item(self,response):

        #print (response.css("div[ id=\"info\"]").extact())
        item=PicItem()
        item['url']=response.url

        item['gericht']=response.css("#info > ul:nth-child(1) > li:nth-child(1) > p:nth-child(2)").css("a[href*=http]::text").extract()
        item['datum'] = response.css(
            "#info > ul:nth-child(1) > li:nth-child(2) > p:nth-child(2)::text").extract()
        item["AZ"]=response.css("#info > ul:nth-child(1) > li:nth-child(3) > p:nth-child(2)::text").extract()
        item['typ']=response.css("#info > ul:nth-child(1) > li:nth-child(4)  ::text").extract()
        item['text']= response.css("#text").extract()
        item['verfahrensgang']=[" ".join(response.css(".instanzen > p:nth-child(2) > a:nth-child(1)::text").extract()+ (response.css(".instanzen > p:nth-child(2) > i:nth-child(2)::text").extract()))]
        item['rechtsgebiete']= response.css(".rechtsgebiete").extract()
        print (item['url'])


        yield item