# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 16:22
# 主页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    keyword_search_text = By.XPATH, '//*[@id="weibo_top_public"]/div/div/div[2]/input'
    click_search_btn = By.XPATH, '//*[@id="weibo_top_public"]/div/div/div[2]/a'

    def input_keyword(self, text):
        self.input_element(self.keyword_search_text, text, 20, 5)

    def click_btn(self):
        self.click_element(self.click_search_btn, 10, 2)
