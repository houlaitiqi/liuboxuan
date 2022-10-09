# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 14:20
"""
1滚动条操作:首先要编写一行js代码
js = "windows.scrollTo(x,y)"
2调用js代码
driver.execute_script(js)
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("file:///D:/TestTest/%E6%B5%8B%E8%AF%95%E6%AD%A3%E5%BC%8F%E8%AF%BE%E5%A0%82%E8%A7%86%E9%A2%91/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html")

sleep(2)
# 编写一行js代码
js = "window.scrollTo(0,200)"
# 调用js代码
driver.execute_script(js)

sleep(2)

driver.quit()
