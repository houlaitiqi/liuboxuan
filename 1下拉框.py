# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 13:10
"""
下拉框操作
先实例化select  导入select包 select = Select(要执行的元素对象)
select.select_by_index(0) 根据下标获取下拉框的内容 索引从0开始
select.select_by_value("") 根据属性获取下拉框的内容  value
select.select_by_visible_text("") 根据下拉框属性值获取下拉框的内容
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("D:\TestTest\测试正式课堂视频\web自动化\素材\注册A.html")

xlk = driver.find_element_by_xpath('//*[@id="selectA"]')
# 实例化下拉框操作
select = Select(xlk)
# # 根据下标获取下拉框内容 索引从0开始
# select.select_by_index(2)
# # # 根据属性进行获取下拉框的内容
# select.select_by_value("sh")
# 根据下拉框文本内容获取下拉框内容
select.select_by_visible_text("A深圳")

sleep(3)
driver.quit()

