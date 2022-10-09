# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 16:27

from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver

    # wait显示等待
    def find_element(self, args, timeout=10, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*args))

    # 文本输入
    def input_element(self, args, text, timeout=10, poll=1):
        self.find_element(args, timeout, poll).send_keys(text)

    # 按钮点击
    def click_element(self, args, timeout=10, poll=1):
        self.find_element(args, timeout, poll).click()

    # 文本内容获取
    def get_text(self, args, timeout=10, poll=1):
        return self.find_element(args, timeout, poll).text

    # 文本内容清除
    def text_clear(self, args):
        self.find_element(args).clear()
