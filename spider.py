import scrapy
from scrapy.linkextractors import LinkExtractor
import csv


class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['agora.co.il', 'yad2.co.il', 'komo.co.il']
    start_urls = ["https://www.agora.co.il", "https://www.yad2.co.il/", 'https://www.komo.co.il/code/y2/']
    custom_settings = {
        'DEPTH_LIMIT': 2  # Limit the depth of crawling
    }

    def _init_(self, *args, **kwargs):
        super(MySpider, self)._init_(*args, **kwargs)
        self.link_extractor = LinkExtractor(allow_domains=self.allowed_domains)

    def parse(self, response):
        # Check if the word "couch" is present in the page content
        if 'ספה' in response.text:
            title = response.css('title::text').get()
            url = response.url
            yield {
                'title': title,
                'url': url
            }
            self.save_to_file(title, url)

        # Follow relevant links
        for link in self.link_extractor.extract_links(response):
            yield response.follow(link, callback=self.parse)

    def is_relevant(self, url):
        # Add your filtering logic here
        # Return True to follow the link, or False to ignore it
        return 'co.il' in url

    def save_to_file(self, title, url):
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([title, url])