# code = UTF-8
# Author:fineSummer
# Date:2021-07-12 15:16

# 27.需求：对《注册实例.html》进行信息注册
# 账号：admin，密码：123456，电话：18600000000，电子邮件：123@qq.com
# 要求：
# 1. 对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
# 2. 定位方式不限
# 3. 暂停3秒钟关闭浏览器 4. 可以不使用PO模式*
import unittest
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94/%E6%B5%8B%E8%AF%95%E6%AD%A3%E5%BC%8F%E8%AF%BE%E5%A0%82%E8%A7%86%E9%A2%91/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

# 主页面
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("18600000000")
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")
sleep(3)
# 切换A
driver.switch_to.frame("myframe1")
# 注册A
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18600000000")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
sleep(3)

# 切换B
driver.switch_to.default_content()
driver.switch_to.frame("myframe2")
# 注册B
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
driver.find_element_by_css_selector("#telB").send_keys("18600000000")
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")
sleep(3)
driver.quit()