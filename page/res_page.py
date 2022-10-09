# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 16:24

# 查询结果页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ResPage(BaseAction):
    res_text = By.XPATH, '//*[@id="pl_feedlist_index"]/div[1]/div[1]/div/div[2]/p[3]/span[3]/a'

    def get_res_text(self):
        return self.get_text(self.res_text)
