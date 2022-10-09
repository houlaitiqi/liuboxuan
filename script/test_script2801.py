# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 16:09

# 1. 打开 weibo.com
# 2. 在输入框中输入“郭德纲”并点击搜索
# 3. 若其微博条数大于2300条，则脚本通过；
import unittest

from time import sleep
from selenium import webdriver

from page.home_page import HomePage
from page.res_page import ResPage


class TestSearch(unittest.TestCase):
    def setUp(self):
        # 选取浏览器
        self.driver = webdriver.Chrome()
        # 获取网址
        self.driver.get("http://www.weibo.com")
        # 静态等待
        self.driver.implicitly_wait(20)

        self.home_page = HomePage(self.driver)
        self.res_page = ResPage(self.driver)

    def tearDown(self):
        # 睡3秒
        sleep(3)
        # 退出
        self.driver.quit()

    def test_search(self):
        # 在输入框输入内容
        # self.home_page.input_keyword_text("郭德纲")
        self.home_page.input_keyword("郭德纲")
        # 点击搜索且点击
        self.home_page.click_btn()

        text = self.res_page.get_res_text()

        assert text >= '2300', '异常'
