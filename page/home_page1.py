# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 17:13

# 主页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage1(BaseAction):
    keyword_search_text1 = By.CLASS_NAME, 'textInput'
    click_search_btn1 = By.XPATH, '//*[@id="search"]/form/div[3]/input'

    def input_keyword1(self, text):
        self.input_element(self.keyword_search_text1, text, 20, 5)

    def click_btn1(self):
        self.click_element(self.click_search_btn1, 10, 2)
