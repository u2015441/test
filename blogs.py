import scrapy


class blogs_spider(scrapy.Spider):
    name = "blogs"
    allowed_domains = ["theblogbowl.in"]
    start_urls = ['http://dada.theblogbowl.in']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        count = len(response.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div/div[1]/h4/span/text()').extract())
        for topics in range(1, count+1, 1):
            item = {
                'Date: ': response.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div/div[1]/h4[' + str(topics) +
                                         ']/span/text()').extract(),
                'Headline: ': response.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div/div[1]/div[' + str(topics) +
                                             ']/h3/a/text()').extract(),
                'Labels: ': response.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div/div[1]/div[' + str(topics) +
                                           ']/div[1]/div[3]/span[1]/a/text()').extract(),
                'Description: ': response.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div/div[1]/div[' + str(topics)
                                                + ']/div[2]/div/text()').extract(),
            }
            yield item
        # follow pagination link
        next_page_url = response.css('a.blog-pager-older-link ::attr(href)').extract_first()
        if next_page_url:
            next_page_url = str(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
