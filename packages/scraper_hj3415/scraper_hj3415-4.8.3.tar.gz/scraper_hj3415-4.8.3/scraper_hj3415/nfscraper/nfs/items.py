# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class C101items(scrapy.Item):
    code = scrapy.Field()
    page = scrapy.Field()

    date = scrapy.Field()
    종목명 = scrapy.Field()
    업종 = scrapy.Field()
    EPS = scrapy.Field()    # 주당순이익 EPS*PER = 주가
    BPS = scrapy.Field()    # 주당장부가치
    PER = scrapy.Field()    # 기업가치가 순이익에 몇배에 거래되는가
    업종PER = scrapy.Field()
    PBR = scrapy.Field()
    배당수익률 = scrapy.Field()

    주가 = scrapy.Field()
    최고52주 = scrapy.Field()
    최저52주 = scrapy.Field()
    거래량 = scrapy.Field()
    거래대금 = scrapy.Field()
    시가총액 = scrapy.Field()
    베타52주 = scrapy.Field()
    발행주식 = scrapy.Field()
    유동비율 = scrapy.Field()
    외국인지분율 = scrapy.Field()

    #기업개요 파트
    intro1 = scrapy.Field()
    intro2 = scrapy.Field()
    intro3 = scrapy.Field()


class C103468items(scrapy.Item):
    code = scrapy.Field()
    page = scrapy.Field()
    df = scrapy.Field()
