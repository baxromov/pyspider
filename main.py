year = [2018, 2019, 2020, 2021, 2022]

months = [
    '01', '02', '03', '04', '05', '06', '07', '08', '09',
    '10', '11', '12'
]

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2022-06-08 02:32:06
# Project: cbu

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        years = [2018, 2019, 2020, 2021, 2022]
        months = [
    '01', '02', '03', '04', '05', '06', '07', '08', '09',
    '10', '11', '12'
]
        for year in years:
            for month in months:
                self.crawl('https://cbu.uz/ru/statistics/intlreserves/?year=2022&month=05&arFilter_DATE_ACTIVE_FROM_1=01.05.2022&arFilter_DATE_ACTIVE_FROM_2=01.06.2022&arFilter_ff%5BSECTION_ID%5D=3493&year={0}&month={1}&set_filter=&set_filter=Y'.format(year, month), callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        #for each in response.doc('a[href^="http"]').items():
        for each in response.doc('body > div.page > section.main > div > div.row > div.col-md-6.col-xl-4.mb_30 > a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        print(response)
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

