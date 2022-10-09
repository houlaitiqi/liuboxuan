# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 13:22
"""
警告框
1对象名 = 浏览器操作对象.switch_to.alert
alert.text   返回弹框的文本信息
alert.accept() 接收对话框选项
alert.dismiss() 取消对话框选项
alert.send_keys() 输入内容
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("file:///D:/TestTest/%E6%B5%8B%E8%AF%95%E6%AD%A3%E5%BC%8F%E8%AF%BE%E5%A0%82%E8%A7%86%E9%A2%91/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html")

jg = driver.find_element_by_xpath('//*[@id="prompta"]').click()

alert = driver.switch_to.alert
# 获取弹框文本
print(alert.text)
# 接收弹框选项
# 取消对话框选项
# print(alert.dismiss())
# 在弹框中文本写入

alert.send_keys("hello")
sleep(3)
alert.accept()
sleep(3)
driver.quit()