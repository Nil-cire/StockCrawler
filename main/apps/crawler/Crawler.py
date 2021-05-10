import abc
import requests


class Crawler:

    def __init__(self):
        pass

    # todo check out all parameters for http request
    @staticmethod
    def craw(url, method, arr=None):
        methods_list = ["get", "post", "put"]
        if method == "get":
            r = requests.get(url)
            try:
                if r.status_code == requests.codes.ok:
                    print(r.text)
                    return r

            except Exception as err:
                print(err)

        if method == "post":
            r = requests.post(url)
            try:
                if r.status_code == requests.codes.ok:
                    print(r.text)
                    self.response = r
                    return r

            except Exception as err:
                print(err)


class TWSECrawler(Crawler):
    @staticmethod
    def craw(url, method, arr=None):
        super().craw(url, method)
