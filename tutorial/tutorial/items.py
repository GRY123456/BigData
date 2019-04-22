# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelItem(scrapy.Item):
    city = scrapy.Field()
    link = scrapy.Field()
    region = scrapy.Field()
    province = scrapy.Field()


class SightItem(scrapy.Item):
    sight_name = scrapy.Field()
    city_name = scrapy.Field()
    rank = scrapy.Field()
    introduction = scrapy.Field()
    play_time = scrapy.Field()
    score = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    open_time = scrapy.Field()
    ticket = scrapy.Field()
    tourism_season = scrapy.Field()
    traffic_guide = scrapy.Field()
    comment_number = scrapy.Field()
    five_mark = scrapy.Field()
    four_mark = scrapy.Field()
    three_mark = scrapy.Field()
    two_mark = scrapy.Field()
    one_mark = scrapy.Field()
    #good_mark = scrapy.Field()
    #medium_mark = scrapy.Field()
    #bad_mark = scrapy.Field()


class NearbyHotelItem(scrapy.Item):
    sight_name = scrapy.Field()
    hotel_name = scrapy.Field()
    distance = scrapy.Field()
    score = scrapy.Field()


class NearbyFoodItem(scrapy.Item):
    sight_name = scrapy.Field()
    restaurant_name = scrapy.Field()
    distance = scrapy.Field()
    score = scrapy.Field()


class NearbySightItem(scrapy.Item):
    sight_name = scrapy.Field()
    nearby_sight_name = scrapy.Field()
    distance = scrapy.Field()
    score = scrapy.Field()


class NearbyMarketItem(scrapy.Item):
    sight_name = scrapy.Field()
    market_name = scrapy.Field()
    distance = scrapy.Field()
    score = scrapy.Field()