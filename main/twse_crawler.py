def url_format(url1, url2, url3 = None, url4 = None, url5 = None, url6 = None):
    list = [url1, url2, url3, url4, url5, url6]
    targetUrl = ""
    for i in list:
        if i is not None:
            targetUrl + str(i)

    return targetUrl


class Crawler():

    def __init__(self):

    def craw(self, targetUrl):
        pass

    def save_to_local(self, localPath):
        pass



a = Crawler()
a.craw("targetUrl")