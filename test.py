from scrapy.http import FormRequest
from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy


class Post_Spider(Spider):
    name = "Post"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):

        token = response.css('input[name="authenticity_token"]::attr(value)')[0].extract()
        data = {'authenticity_token': token,
                'login': 'ali-gillani',
                'password': 'aliali786'}
        yield FormRequest.from_response(response,
                                        formdata=data,
                                        callback=self.parse_repo
                                        )

    def parse_repo(self, response):
        """This will fetch all the teams and repos of the user"""
        open_in_browser(response)
        self.record = {
            'Teams': response.css('span.width-fit::text').extract(),
            'All repositories': response.css('a.d-flex::attr(href)').extract(),
        }
        yield self.record
        yield scrapy.Request(url='https://github.com/ali-gillani/test/pulls', callback=self.parse_pull)

    def parse_pull(self, response):
        """This will fetch all the pull requests in the-lab"""
        open_in_browser(response)
        number_of_elements = len(response.css('a.link-gray-dark::text').extract())
        for number in range(0, number_of_elements):
            pull_request= {
                'Pull name': response.css('a.link-gray-dark::text')[number].extract(),
                'Pull link': response.css('a.link-gray-dark::attr(href)')[number].extract()
            }
            yield pull_request