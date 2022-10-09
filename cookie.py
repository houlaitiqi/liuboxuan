# code = UTF-8
# Author:xiaoLiu
# Date:2022-01-12 15:33
"""
浏览器向服务器发送请求
服务器处理cookie并将cookie保存在浏览器端
浏览器在此发送任何一个请求都会带上cookie
服务器收到请求并响应
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
# 获取所有的cookie
# print(driver.get_cookies())
driver.maximize_window()

driver.add_cookie({"name": "sensorsdata2015jssdkcross", "value": "%7B%22distinct_id%22%3A%2217b612bee4a17-0e870ef5acfbff-4343363-1327104-17b612bee4b155%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%22%2C%22%24latest_utm_source%22%3A%22%E7%99%BE%E5%BA%A6SEM%22%2C%22%24latest_utm_medium%22%3A%22%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22%24latest_utm_campaign%22%3A%22%E5%B8%B8%E8%A7%84%E6%8A%95%E6%94%BE%22%2C%22%24latest_utm_content%22%3A%22%E8%A1%8C%E4%B8%9A%E8%AF%8D%2B%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%22%2C%22%24latest_utm_term%22%3A%22mysql%E6%9C%8D%E5%8A%A1%E5%90%AF%E5%8A%A8%22%7D%2C%22%24device_id%22%3A%2217b612bee4a17-0e870ef5acfbff-4343363-1327104-17b612bee4b155%22%7D"})

driver.add_cookie({"name": "__DC_gid", "value": "177231408.679557149.1628481719285.1629339946450.62"})

sleep(3)

driver.refresh()

driver.quit()