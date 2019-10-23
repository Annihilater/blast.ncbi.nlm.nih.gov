#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/23 13:37
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 2.py

import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    await page.screenshot(path='../data/img/example.png')
    await page.pdf(path='../data/pdf/example.pdf')  # 打印 pdf 需要把 headless 关闭
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
