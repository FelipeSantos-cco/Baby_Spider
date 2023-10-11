import scrapy


class BoletinsecSpider(scrapy.Spider):
    name = "Boletinsec"
    allowed_domains = ["boletimsec.com.br"]
    start_urls = ["https://boletimsec.com.br"]

    def parse(self, response):
        pass
