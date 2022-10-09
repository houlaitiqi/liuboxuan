# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 16:16
"""
截图 driver.get_screenshot_as_file("图片的路径") 这样截图可能会覆盖
所以要引入一个时间戳 time 时间戳不会被覆盖
"""
from selenium import webdriver
from time import sleep, time

driver = webdriver.Chrome()

driver.get("file:///D:/TestTest/%E6%B5%8B%E8%AF%95%E6%AD%A3%E5%BC%8F%E8%AF%BE%E5%A0%82%E8%A7%86%E9%A2%91/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html")

driver.find_element_by_xpath('//*[@id="userA"]').send_keys("admin11")

driver.find_element_by_xpath('//*[@id="passwordA"]').send_keys("12345676543")
# 时间戳是f类型
t = time()
driver.get_screenshot_as_file("file/%s.png" % t)

sleep(2)
driver.quit()
