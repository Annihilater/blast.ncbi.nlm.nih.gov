#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/23 11:16
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : main.py

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def login(self):
#     """
#     使用 selenium 自动登录
#     :param self:
#     :return:
#     """
#     driver = webdriver.Chrome()
#     driver.get(self.form_url)
#
#     sign_in = driver.find_element_by_id('myncbi_sign_in_0')
#     sign_in.click()
#
#     user_name = driver.find_element_by_id('uname')
#     user_name.send_keys(self.account)
#
#     pwd = driver.find_element_by_id('upasswd')
#     pwd.send_keys(self.pwd)
#
#     button = driver.find_element_by_id('signinBtn')
#     button.click()
#     return driver


def auto_submit(path):
    form_url = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'

    # selenium 设置无界面参数 --headless
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)

    # 有界面 selenium
    driver = webdriver.Chrome()
    driver.get(form_url)

    upload = driver.find_element_by_id('upl')
    upload.send_keys(path)
    print(upload.get_attribute('value'))

    submit = driver.find_element_by_id('b1')
    submit.click()

    # 等待 8 秒，等待响应页面出现提交时间
    # time.sleep(8)

    print('开始等待 rid 和 submit_time 加载')
    rid = driver.find_element_by_css_selector('#statInfo tbody tr:nth-child(1) td:nth-child(2) b').text

    # 等待 submit_time 加载，每隔一秒检测一次
    while True:
        time.sleep(1)
        submit_time = driver.find_element_by_css_selector('#statInfo tbody tr:nth-child(3) td:nth-child(2)').text
        print(1)
        if submit_time != '00:00:00':
            break

    print('rid 和 submit_time 加载完成')
    print(submit_time + ': ' + rid + '\n')

    print('开始写入 records')
    with open('data/txt/rid_records.txt', 'a') as f:
        f.write(submit_time + ': ' + rid + '\n')
    print('records 写入完成' + '\n')

    print('开始写入等待页面')
    wait_html = driver.page_source
    with open('data/html/wait.html', 'w') as f:
        f.write(wait_html)
    print('等待页面写入完成' + '\n')

    # 等待结果页面加载完成
    print('开始等待结果页面')
    WebDriverWait(driver, timeout=100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#brc h1')))
    print('结果页面等待完成' + '\n')

    print('开始写入结果页面')
    result_html = driver.page_source
    with open('data/html/result.html', 'w') as f:
        f.write(result_html)
    print('结果页面写入完成' + '\n')

    time.sleep(2)
    driver.close()
    return rid


if __name__ == '__main__':
    file_path = '/Users/stefanannihilater/Dropbox/PycharmProjects/blast/data/fa/1.fa'
    print(auto_submit(file_path))
