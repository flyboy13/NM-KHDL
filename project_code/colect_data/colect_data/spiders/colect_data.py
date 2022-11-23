import scrapy
import json

class collect_player_info(scrapy.Spider):
    name='players_info'
    page_count = 2
    num_page = 100 #Num of page need to get data

    def start_requests(self):
        urls = ['https://www.nhatot.com/thue-phong-tro-tp-ho-chi-minh?page=1']
        # YOUR CODE HERE
        yield scrapy.Request(urls[0], callback=self.parse)
  
    def parse(self, response):
        # YOUR CODE HERE
    
        yield 
        if self.page_count < self.num_page:
            next_page_url = 'https://www.nhatot.com/thue-phong-tro-tp-ho-chi-minh?page=' + self.page_count
            self.page_count += 1
            yield scrapy.Request(next_page_url, callback=self.parse) 