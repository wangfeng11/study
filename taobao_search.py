#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pathlib import Path
import time

# import HTMLReport

# 获取百度
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
driver.get("https://www.baidu.com")
print('driver.name:', driver.name)
print('baidu title:', driver.title)
pageBaidu = driver.current_window_handle
print('pageBaidu:', pageBaidu)
elem = driver.find_element_by_name('wd')
sleep(3)
# 输入淘宝
input_taobao = elem.send_keys('淘宝')
# 点击搜索
elem.send_keys(Keys.RETURN)
# search_taobao = driver.find_element_by_id('su').click()
print('search url', driver.current_url)
print('title:', driver.title)
# 等待搜索时间            直到检查到下一个页面的元素"a.c-showurl"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.c-showurl")))
print("search page url:", driver.current_url)  # 获取当前加载页面的 URL
# 定位css_selector为“a.c-showurl”,结果为一个所有css_selector为“a.c-showurl”的列表
click_taobao = driver.find_elements_by_css_selector("a.c-showurl")
# 点击列表中的第一个
click_taobao[0].click()
print("results:", click_taobao)
sleep(3)
pageBaidu = driver.current_window_handle
print('pageBaidu:', pageBaidu)
page_Baidu_Taobao = driver.window_handles
print('page_Baidu_Taobao:', page_Baidu_Taobao)
# 定位到淘宝页面
driver.switch_to.window(page_Baidu_Taobao[1])
pageTaobao = driver.current_window_handle
print('pageTaobao:', pageTaobao)
#sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
# 定位输入框，并输入搜索关键字“图书”
book = driver.find_elements_by_css_selector('#q')
book[0].send_keys('图书')
print('book:', book)
click_book = book[0].send_keys(Keys.RETURN)
sleep(2)
backTaobao = driver.back()
pageTaobao = driver.current_window_handle
print('pageTaobao:', pageTaobao)
page_Baidu_Taobao = driver.window_handles
print('page_Baidu_Taobao:', page_Baidu_Taobao)
driver.switch_to.window(page_Baidu_Taobao[0])
pageBaidu = driver.current_window_handle
print('pageBaidu:', pageBaidu)
sleep(3)
# 清空关键词图书记录，并重新输入关键词'python'
clear_book = elem.clear()
python = elem.send_keys('python')
elem.send_keys(Keys.RETURN)
# search_python = driver.find_element_by_id('su').click()
sleep(3)
current_time = time.strftime("%Y%m%d_%H-%M-%S", time.localtime(time.time()))
scrpath = "D:\\download\\images"  # 指定的保存目录
capturename = '\\' + current_time + '.png'  # 自定义命名截图
wholepath = scrpath + capturename
print(wholepath)
if Path(scrpath).is_dir():  # 判断文件夹路径是否已经存在
    pass
else:
    Path(scrpath).mkdir()  # 如果不存在，创建文件夹
driver.save_screenshot(wholepath)  # 不能接受Path类的值，只能是字符串，否则无法截图
sleep(3)
driver.quit()
