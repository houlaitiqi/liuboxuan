# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 17:13
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ResPage1(BaseAction):
    res_text1 = By.XPATH, '//*[@id="2"]/h3/a'

    def get_res_text1(self):
        return self.get_text(self.res_text1)
