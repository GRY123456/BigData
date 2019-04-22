# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TravelItem
from tutorial.items import SightItem
from tutorial.items import NearbyHotelItem
from tutorial.items import NearbyFoodItem
from tutorial.items import NearbySightItem
from tutorial.items import NearbyMarketItem
import json



class TravelSpider(scrapy.Spider):
    name = 'travel'
    allowed_domains = ['travel.qunar.com']
    start_urls = ['http://travel.qunar.com/place/?from=header']

    def parse(self, response):
        regions = response.css('.list.current .contbox.current .listbox')
        for region in regions:
            region_name = region.css('.hd::text').extract_first()
            provinces = region.css('.ct .sub_list')
            for province in provinces:
                if region_name == '直辖市':
                    province_name = '直辖市'
                else:
                    province_name = province.css('.titbox .tit::text').extract_first().replace('\u00a0', '')[:-1]
                citys = province.css('.list_item.clrfix .item')
                for city in citys:
                    city_name = city.css('.link::text').extract_first()
                    city_link = city.css('a::attr("href")').extract_first()
                    item = TravelItem()
                    item['city'] = city_name
                    item['link'] = city_link
                    item['region'] = region_name
                    item['province'] = province_name
                    yield item
        with open('E:/python_work/tutorial/data_cn2.json', 'r', encoding='utf-8') as f:
            load_dict = json.load(f)
            link_index = 0
            while link_index < len(load_dict):
            # while link_index < 1:
                url = load_dict[link_index]['link'] + '-jingdian'
                # url = 'http://travel.qunar.com/p-cs299914-beijing-jingdian'

                link_index = link_index + 1
                yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
        links = response.css('.titbox.clrfix .titlink::attr("href")').extract()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse3)
        url = response.css('.page.next::attr("href")').extract_first()
        yield scrapy.Request(url=url, callback=self.parse2)

    def parse3(self, response):
        item = SightItem()
        item['sight_name'] = response.css('.b_title.clrfix .tit::text').extract_first()
        if len(response.css('.b_crumbs .e_crumbs .clrfix .item.pull .txtlink::text').extract()) > 1:
            item['city_name'] = response.css('.b_crumbs .e_crumbs .clrfix .item.pull .txtlink::text').extract()[1]
        else:
            item['city_name'] = None
        item['rank'] = response.css('div.b_focus div div.e_focus_txtbox div.txtbox div.ranking span::text').extract_first()
        item['introduction'] = "".join(response.css('#gs div.e_db_content_box p::text').extract())
        item['play_time'] = response.css('div.txtbox div.time::text').extract_first()
        item['score'] = response.css('div.scorebox.clrfix span.cur_score::text').extract_first()
        item['address'] = response.css('td.td_l dl dd span::text').extract_first()
        if len(response.css('td.td_l dl dd span::text').extract()) >= 2:
            item['phone'] = response.css('td.td_l dl dd span::text').extract()[1]
        else:
            item['phone'] = None
        item['open_time'] = response.css('td.td_r dl dd span p::text').extract_first()
        item['ticket'] = response.css('#mp div.e_db_content_box.e_db_content_dont_indent p::text').extract_first()
        item['tourism_season'] = response.css('#lysj div.e_db_content_box.e_db_content_dont_indent p::text').extract_first()
        item['traffic_guide'] = "".join(response.css('#jtzn div.e_db_content_box.e_db_content_dont_indent *::text').extract())
        item['comment_number'] = response.css('div.b_detail_section.b_detail_comment div.e_title_box h3 span::text').extract_first()
        item['five_mark'] = response.css(
            '#detail_box div.b_detail_section.b_detail_comment div.star-filter div ul li div div::attr("style")').extract()[0]
        item['four_mark'] = response.css(
            '#detail_box div.b_detail_section.b_detail_comment div.star-filter div ul li div div::attr("style")').extract()[1]
        item['three_mark'] = response.css(
            '#detail_box div.b_detail_section.b_detail_comment div.star-filter div ul li div div::attr("style")').extract()[2]
        item['two_mark'] = response.css(
            '#detail_box div.b_detail_section.b_detail_comment div.star-filter div ul li div div::attr("style")').extract()[3]
        item['one_mark'] = response.css(
            '#detail_box div.b_detail_section.b_detail_comment div.star-filter div ul li div div::attr("style")').extract()[4]
        yield item
        sight_item = NearbySightItem()
        sights = response.css('ul.list_item.current .item')
        for sight in sights:
            sight_item['sight_name'] = response.css('.b_title.clrfix .tit::text').extract_first()
            sight_item['nearby_sight_name'] = sight.css('div.t.clrfix a::text').extract_first()
            sight_item['distance'] = sight.css('div span.distance::text').extract_first()
            sight_item['score'] = sight.css('div.t span.total_star span::attr("style")').extract_first()
            yield sight_item
        food_item = NearbyFoodItem()
        hotel_item = NearbyHotelItem()
        market_item = NearbyMarketItem()
        tem_items = response.css('#idContBox ul.list_item')
        sum = 0
        for tem_item in tem_items:
            if sum == 1:
                foods = tem_item.css('.item')
                for food in foods:
                    food_item['sight_name'] = response.css('.b_title.clrfix .tit::text').extract_first()
                    food_item['restaurant_name'] = food.css('div.t.clrfix a::text').extract_first()
                    food_item['distance'] = food.css('div span.distance::text').extract_first()
                    food_item['score'] = food.css('div.t span.total_star span::attr("style")').extract_first()
                    yield food_item
            elif sum == 2:
                hotels = tem_item.css('.item')
                for hotel in hotels:
                    hotel_item['sight_name'] = response.css('.b_title.clrfix .tit::text').extract_first()
                    hotel_item['hotel_name'] = hotel.css('div.t.clrfix a::text').extract_first()
                    hotel_item['distance'] = hotel.css('div span.distance::text').extract_first()
                    hotel_item['score'] = hotel.css('div.t span.total_star span::attr("style")').extract_first()
                    yield hotel_item
            elif sum == 3:
                markets = tem_item.css('.item')
                for market in markets:
                    market_item['sight_name'] = response.css('.b_title.clrfix .tit::text').extract_first()
                    market_item['market_name'] = market.css('div.t.clrfix a::text').extract_first()
                    market_item['distance'] = market.css('div span.distance::text').extract_first()
                    market_item['score'] = market.css('div.t span.total_star span::attr("style")').extract_first()
                    yield market_item
            sum = sum + 1