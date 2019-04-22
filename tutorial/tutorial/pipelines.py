# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os


class CoolscrapyPipeline(object):

    def __init__(self):
        if os.path.exists('data_cn1.json'):
            with open('data_cn1.json', 'w', encoding='utf-8') as f:
                f.write("")
        if os.path.exists('data_cn3.json'):
            with open('data_cn3.json', 'w', encoding='utf-8') as f:
                f.write("")
        if os.path.exists('data_hotel.json'):
            with open('data_hotel.json', 'w', encoding='utf-8') as f:
                f.write("")
        if os.path.exists('data_food.json'):
            with open('data_food.json', 'w', encoding='utf-8') as f:
                f.write("")
        if os.path.exists('data_nearby_sight.json'):
            with open('data_nearby_sight.json', 'w', encoding='utf-8') as f:
                f.write("")
        if os.path.exists('data_market.json'):
            with open('data_market.json', 'w', encoding='utf-8') as f:
                f.write("")

    def process_item(self, item, spider):
        if type(item).__name__ == 'TravelItem':
            with open('data_cn1.json', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False)
                f.write(',\n')
            return item

        if type(item).__name__ == 'SightItem':
            with open('data_cn3.json', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False)
                f.write(',\n')
            return item

        if type(item).__name__ == 'NearbyHotelItem':
            with open('data_hotel.json', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False)
                f.write(',\n')
            return item

        if type(item).__name__ == 'NearbyFoodItem':
            with open('data_food.json', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False)
                f.write(',\n')
            return item

        if type(item).__name__ == 'NearbySightItem':
            with open('data_nearby_sight.json', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False)
                f.write(',\n')
            return item

        if type(item).__name__ == 'NearbyMarketItem':
            with open('data_market.json', 'a', encoding='utf-8') as f:
                json.dump(dict(item), f, ensure_ascii=False)
                f.write(',\n')
            return item


    def close_spider(self, spider):
        '''
        with open('data_cn1.json', 'r', encoding='utf-8') as f1:
            len_f1 = len(f1.readlines())

        with open('data_cn1.json', 'r', encoding='utf-8') as f1:
            with open('data_cn2.json', 'w', encoding='utf-8') as f2:
                sum = 0
                for line in f1:
                    if sum == 0:
                        f2.write('[\n')
                        f2.write(line)
                    elif sum == len_f1 - 1:
                        f2.write(line[:-2])
                        f2.write('\n]')
                    else:
                        f2.write(line)
                    sum = sum + 1

        with open('data_cn3.json', 'r', encoding='utf-8') as f3:
            len_f3 = len(f3.readlines())

        with open('data_cn3.json', 'r', encoding='utf-8') as f3:
            with open('data_cn4.json', 'w', encoding='utf-8') as f4:
                sum = 0
                for line in f3:
                    if sum == 0:
                        f4.write('[\n')
                        f4.write(line)
                    elif sum == len_f3 - 1:
                        f4.write(line[:-2])
                        f4.write('\n]')
                    else:
                        f4.write(line)
                    sum = sum + 1
        '''''