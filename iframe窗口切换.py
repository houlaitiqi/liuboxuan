# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 15:02
"""
iframe就是页面中嵌套了一个页面
driver.switch_to_frame("iframe里面的id和name") 切换到指定页面
driver.switch_to_default_content() 切换到首页

"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("D:\TestTest\测试正式课堂视频\web自动化\素材\注册实例.html")
# 在首页输入内容
driver.find_element_by_xpath('//*[@id="user"]').send_keys("admin")
sleep(3)
# 切换到frame里面的页面进行输入内容()参数可以为frame里面的id和name
driver.switch_to.frame("myframe1")
sleep(3)
driver.find_element_by_xpath('//*[@id="userA"]').send_keys("admin")
sleep(3)
# 切换到当前页面进行定位和输入
driver.switch_to_default_content()
driver.find_element_by_xpath('//*[@id="password"]').send_keys("2345643213456")
sleep(3)
driver.quit()