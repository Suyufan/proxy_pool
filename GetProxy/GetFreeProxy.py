import requests
import re
from Util import HelpFunction


class FreeProxy(object):
    def __init__(self):
        pass

    @staticmethod
    def getFirstFreeProxy(self, pagenum=5):
        url_list = ('http://www.kuaidaili.com/free/inha/{page}/'.format(page=page) for page in range(1, pagenum + 1))
        for url in url_list:
            tree = HelpFunction.getHTMLTree(url)
            proxy_list = tree.xpath('//div[@id="list"]//tbody/tr')
            for proxy in proxy_list:
                print(':'.join(proxy.xpath('./td/text()')[0:2]))

    @staticmethod
    def getSecondFreeProxy(self, pagenum=5):
        url_list_nn = ('http://www.xicidaili.com/nn/{page}/'.format(page=page) for page in range(1, pagenum + 1))
        url_list_nr = ('http://www.xicidaili.com/nt/{page}/'.format(page=page) for page in range(1, pagenum + 1))
        url_list_all = [url_list_nn, url_list_nr]
        for url_list in url_list_all:
            for url in url_list:
                # print(url)
                tree = HelpFunction.getHTMLTree(url)
                proxy_list = tree.xpath('//table[@id="ip_list"]//tr[@class="odd"]')
                print(len(proxy_list))

                for proxy in proxy_list:
                    print(':'.join(proxy.xpath('./td/text()')[0:2]))

if __name__ == "__main__":
    free_proxy = FreeProxy()
    free_proxy.getSecondFreeProxy(self=free_proxy)
