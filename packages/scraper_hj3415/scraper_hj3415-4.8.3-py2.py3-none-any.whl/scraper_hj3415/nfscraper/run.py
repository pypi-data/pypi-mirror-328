import os
from scrapy.crawler import CrawlerProcess
from webdriver_hj3415 import drivers

from scraper_hj3415.nfscraper.nfs.spiders.c101 import C101Spider
from scraper_hj3415.nfscraper.nfs.spiders.c106 import C106Spider
from scraper_hj3415.nfscraper.nfs.spiders.c103 import C103YSpider, C103QSpider
from scraper_hj3415.nfscraper.nfs.spiders.c104 import C104YSpider, C104QSpider
from scraper_hj3415.nfscraper.nfs.spiders.c108 import C108Spider

from utils_hj3415 import setup_logger

mylogger = setup_logger(__name__, 'WARNING')

# 세팅파일을 프로젝트의 settings.py를 사용하지 않고 직접 만들어서 사용하는 방법.
# 대신 nfs 모듈을 찾을수 있도록 sys에 경로를 추가해 줘야 한다.
import sys
from pathlib import Path
# Scrapy 프로젝트 경로 추가
sys.path.append(str(Path(__file__).resolve().parent))

settings = {
'BOT_NAME': "nfs",

'SPIDER_MODULES': ["nfs.spiders"],
'NEWSPIDER_MODULE': "nfs.spiders",


'ROBOTSTXT_OBEY': False,
'ITEM_PIPELINES': {
    "nfs.pipelines.ValidationPipeline": 300,
    "nfs.pipelines.RedisPipeline": 400,
    "nfs.pipelines.MongoPipeline": 500,
},
'TWISTED_REACTOR': "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
'FEED_EXPORT_ENCODING': "utf-8",

'LOG_ENABLED': True,
'LOG_LEVEL' : 'ERROR',
}

BROWSER = os.getenv("BROWSER", 'chrome')
HEADLESS = os.getenv('HEADLESS', 'True').lower() in ("true", "1", "yes")
CHROMEDRIVER_VERSION = os.getenv('CHROMEDRIVER_VERSION')



def c101(*args):
    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C101Spider, codes=args)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

def c106(*args):
    webdriver = drivers.get(browser=BROWSER, driver_version=CHROMEDRIVER_VERSION, headless=HEADLESS)

    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C106Spider, codes=args, webdriver=webdriver)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

    mylogger.info('Retrieve webdriver...')
    webdriver.quit()

def c103y(*args):
    webdriver = drivers.get(browser=BROWSER, driver_version=CHROMEDRIVER_VERSION, headless=HEADLESS)

    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C103YSpider, codes=args, webdriver=webdriver)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

    mylogger.info('Retrieve webdriver...')
    webdriver.quit()

def c103q(*args):
    webdriver = drivers.get(browser=BROWSER, driver_version=CHROMEDRIVER_VERSION, headless=HEADLESS)

    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C103QSpider, codes=args, webdriver=webdriver)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

    mylogger.info('Retrieve webdriver...')
    webdriver.quit()

def c104y(*args):
    webdriver = drivers.get(browser=BROWSER, driver_version=CHROMEDRIVER_VERSION, headless=HEADLESS)

    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C104YSpider, codes=args, webdriver=webdriver)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

    mylogger.info('Retrieve webdriver...')
    webdriver.quit()

def c104q(*args):
    webdriver = drivers.get(browser=BROWSER, driver_version=CHROMEDRIVER_VERSION, headless=HEADLESS)

    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C104QSpider, codes=args, webdriver=webdriver)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

    mylogger.info('Retrieve webdriver...')
    webdriver.quit()

def c108(*args):
    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    process.crawl(C108Spider, codes=args)
    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

def all_spider(*args):
    spiders = (C101Spider, C106Spider, C103YSpider, C103QSpider, C104YSpider, C104QSpider, C108Spider)
    wedrivers = []

    # Scrapy 설정 가져오기
    # settings = get_project_settings()
    # CrawlerProcess 인스턴스 생성
    process = CrawlerProcess(settings)
    # 스파이더 추가 및 실행
    for Spider in spiders:
        if Spider == C101Spider or Spider == C108Spider:
            process.crawl(Spider, codes=args)
        else:
            webdriver = drivers.get(browser=BROWSER, driver_version=CHROMEDRIVER_VERSION, headless=HEADLESS)
            process.crawl(Spider, codes=args, webdriver=webdriver)
            wedrivers.append(webdriver)

    process.start()  # 블로킹 호출, 스파이더가 완료될 때까지 기다림

    for webdriver in wedrivers:
        mylogger.info('Retrieve webdriver...')
        webdriver.quit()
