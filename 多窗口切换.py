# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 15:18
"""
多窗口切换
driver.window.handles   获取所有的页面
driver.current.window.handle  获取当前页面
driver.switch_to.window(driver.window.handles[0]) 切换到指定页面
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("file:///D:/TestTest/%E6%B5%8B%E8%AF%95%E6%AD%A3%E5%BC%8F%E8%AF%BE%E5%A0%82%E8%A7%86%E9%A2%91/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html")

driver.find_element_by_xpath('//*[@id="fw"]').click()

sleep(3)

driver.find_element_by_xpath('//*[@id="fw"]').click()

sleep(10)
# 获取所有窗口的
print(driver.window_handles)
# 获取当前窗口的页面(首页)
print(driver.current_window_handle)
# 切换到指定页面
driver.switch_to.window(driver.window_handles[0])
sleep(3)
driver.quit()