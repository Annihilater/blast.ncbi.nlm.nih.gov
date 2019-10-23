#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/23 13:33
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : 1.py
import asyncio
import time

from pyppeteer import launch


async def main():
    url = 'https://www.zhihu.com'

    browser = await launch(
        {'headless': False, 'dumpio': True, 'autoClose': False, 'args': ['--no-sandbox', '--window-size=1366,850']})
    page = await browser.newPage()

    # 设置页面视图大小
    await page.setViewport({'width': 1366, 'height': 768})

    # 是否启用 Js 渲染
    await page.setJavaScriptEnabled(enabled=True)
    print('ok2')

    await page.goto(url)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
