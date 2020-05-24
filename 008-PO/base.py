import time


class BasePage:
    '''
    基础的page层，封装一些常用方法
    '''
    def __init__(self,driver):
        self.driver=driver

    #打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    #id定位
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

        # xpath定位

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

        # 获取title
    def get_title(self):
        return self.driver.title

        # 封装休眠时间
    def sleep(self, sec):
        time.sleep(sec)