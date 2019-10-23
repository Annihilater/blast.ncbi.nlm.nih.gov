#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/23 13:00
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : auto_submit.py
import asyncio
from pyppeteer import launch


async def main(path):
    form_url = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'
    browser = await launch({
        'headless': False,
        'dumpio': True,
        'autoClose': False,
        'args': ['--no-sandbox', '--window-size=1000,1200']
    })

    page = await browser.newPage()
    # 设置页面视图大小
    await page.setViewport({'width': 1000, 'height': 1200})
    print('ok')

    # 是否启用 Js 渲染
    await page.setJavaScriptEnabled(enabled=True)
    print('ok2')

    await page.goto(form_url)
    print('ok3')

    # 上传文件
    upload = await page.querySelector('#upl')
    await upload.uploadFile(path)

    # 点击提交
    submit = await page.querySelector('#b1')
    await submit.click()
    print('点击提交成功')
    rid_selector = '#statInfo tbody tr:nth-child(1) td:nth-child(2) b'
    submit_time_selector = '#statInfo tbody tr:nth-child(3) td:nth-child(2)'
    await page.waitForSelector(rid_selector, visible=True, timeout=60000)
    await page.waitForSelector(submit_time_selector, visible=True, timeout=6000)
    rid = await page.evaluate('() = > document.querySelector({}).innerText'.format(rid_selector))
    submit_time = await page.evaluate('() = > document.querySelector({}).innerText'.format(submit_time_selector))
    print('rid 和 submit_time 加载完成')
    print(submit_time + ': ' + rid + '\n')

    print('开始写入 records')
    with open('../data/txt/rid_records.txt', 'a') as f:
        f.write(submit_time + ': ' + rid + '\n')
    print('records 写入完成' + '\n')

    print('开始写入等待页面')
    wait_html = await page.content()
    with open('../data/html/wait.html', 'w') as f:
        f.write(str(wait_html))
    print('等待页面写入完成' + '\n')

    print('开始等待结果页面')
    await page.waitForSelector('#brc h1')
    result_html = await page.content()
    with open('../data/html/result.html', 'w') as f:
        f.write(str(result_html))
    print('结果页面写入完成' + '\n')

    await browser.close()


path = '/Users/stefanannihilater/Dropbox/PycharmProjects/blast/data/fa/1.fa'
asyncio.get_event_loop().run_until_complete(main(path))
