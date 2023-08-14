# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 14:12
@Auth ： 仔仔
@File ：main.py
@Description ：
"""
import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import BrowserContext

USERNAME_BTN_ID = r"loginName"
PASSWORD_BTN_ID = r"loginPassword"
ALIYUN_LOGIN_COOKIE_NAME = r"login_aliyunid_ticket"
RDS_LOGIN_COOKIE_NAME = r"__DMS_USER_LOGIN_COOKIE_KEY__"
ALIYUN_LOGIN_URL = r"https://signin.aliyun.com/login.htm#/main"
RDS_LOGIN_URL = r"https://dms.console.aliyun.com/#/dms/login"


async def main():
    async with async_playwright() as p:
        # if p.chromium
        # browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        # context = browser.contexts[0]

        context = await p.chromium.launch_persistent_context(
            executable_path='/Applications/QQBrowser.app/Contents/MacOS/QQBrowser',
            user_data_dir='./user_data_dir',
            headless=False,
            args=[],
        )

        page = await context.new_page()
        await page.goto(ALIYUN_LOGIN_URL)
        async with page.expect_navigation(wait_until='load', timeout=2000):
            print("title:", await page.title())
        # aliyun_login_page = await new_page.value
        # await aliyun_login_page.wait_for_load_state()
        # try:
        #     await aliyun_login_page.wait_for_url(ALIYUN_LOGIN_URL, timeout=9000, wait_until='load')
        # except Exception as e:
        #     print('e:', e)
        #     print('title:', aliyun_login_page.title())

        # print(await aliyun_login_page.title())
        print("ccccccccccc")
        input("等待关闭......")
        print("sssssss")
        await page.wait_for_timeout(1000000)


if __name__ == '__main__':
    asyncio.run(main())
