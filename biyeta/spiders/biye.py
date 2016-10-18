# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from scrapy.http import Request
from ..items import BiyetaItem
from .. import settings

USER_NAME = 'sonju2011@gmail.com'
PASSWORD = 'sonju10@'
BASE_URL = 'http://www.biyeta.com'


class BiyeSpider(scrapy.Spider):
    name = 'biye'
    allowed_domains = ['biyeta.com']
    start_urls = [BASE_URL + '/login']
    next_page = 1
    count = 0

    def parse(self, response):
        token = response.css('input[name=authenticity_token]::attr(value)').extract_first()
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form[@id="new_user"]',
            formdata={
                'user[email]': settings.USER_NAME,
                'user[password]': settings.PASSWORD,
                'authenticity_token': token,
            },
            callback=self.after_login
        )

    def create_ajax_request(self, page_number):
        ajax_template = BASE_URL+'/general_search/index?page={profile_id}'
        url = ajax_template.format(profile_id=page_number)
        return Request(url=url, callback=self.after_login)

    def after_login(self, response):
        pagination = response.xpath('//div[@class="pagination"]/a//text()')
        page = pagination[-2].extract() if pagination else 0

        for link in response.xpath('//ul[@id="result_container"]/li//@href').extract():
            url = urljoin(response.url, link)
            yield Request(url=url, callback=self.action)

        if self.next_page < int(page):
            self.next_page += 1
            yield self.create_ajax_request(self.next_page)

    def action(self, response):
        item = BiyetaItem()
        item['name'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[1]/div[2]//text()').extract()[0].strip()
        item['about'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[1]//text()').extract()[0].strip()
        item['age'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[5]/span[2]//text()').extract()[0].strip()
        item['district'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[3]/span[2]//text()').extract()[0].strip()
        item['height'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[6]/span[2]//text()').extract()[0].strip()
        item['occupation'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[1]/span[2]//text()').extract()[0].strip()
        item['education'] = response.xpath('//body/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[7]/span[2]//text()').extract()[0].strip()
        item['url'] = response.url

        return item