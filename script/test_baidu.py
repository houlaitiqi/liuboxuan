# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 17:05

import unittest

from time import sleep
from selenium import webdriver

from page.home_page1 import HomePage1
from page.res_page1 import ResPage1


# 脚本2：
# 1. 打开 baidu.com
# 2. 点击左上角的 “hao123”
# 3. 在百度搜索框中输入“国庆节”并点击“百度一下”
# 4. 若链接标题中出现 “国庆节_百度百科”，则脚本通过
class TestSearch(unittest.TestCase):
    def setUp(self):
        # 选取浏览器
        self.driver = webdriver.Chrome()
        # 获取网址
        self.driver.get("http://www.hao123.com")
        # 静态等待
        self.driver.implicitly_wait(20)

        self.home_page1 = HomePage1(self.driver)
        self.res_page1 = ResPage1(self.driver)

    def tearDown(self):
        # 睡3秒
        sleep(3)
        # 退出
        self.driver.quit()

    def test_search(self):
        # self.driver.switch_to.frame("g-ib searchForm form-hook")
        self.home_page1.input_keyword1("国庆节")
        # 点击搜索且点击
        self.home_page1.click_btn1()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.res_page1.get_res_text1()

        print(text)

        assert text == "国庆节 - 百度百科", '异常'
