from main.apps.crawler.Crawler import Crawler, TWSECrawler
from datetime import datetime, date


class MainControlManager:

    crawler = Crawler()
    today = date.today()

    def __init__(self):
        pass

    def search_stock_by_date(self, stock_id: str, date):

        pass

    def search_stock_by_date_period(self, stock_id: str, date_start, date_end):
        pass

