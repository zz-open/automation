# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from playwright.async_api import Playwright, async_playwright, expect
from common.utils import parse_yaml

DEBUG = True
LOCAL_ALI_DMS_LOGIN_CONF_FILE_PATH = r"E:\jungle\project_conf\ali_dms_login_conf.yaml"
if DEBUG:
    conf = parse_yaml(LOCAL_ALI_DMS_LOGIN_CONF_FILE_PATH)
else:
    conf = parse_yaml(f"{os.getcwd()}/conf.yaml")

username = conf.get('username', "")
password = conf.get('password', "")
timeout = conf.get("timeout", 1000 * 60 * 60 * 24)
# stealth.min.js文件的存放路径
STEALTH_PATH = f"{os.getcwd()}/../common/stealth.min.js"


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False, chromium_sandbox=False,
                                               ignore_default_args=["--enable-automation"],
                                               channel="chrome", )
    ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
          'Safari/537.36')
    context = await browser.new_context(user_agent=ua)
    # 添加初始化脚本
    await context.add_init_script(path=STEALTH_PATH)
    page = await context.new_page()
    # 阿里云子账号平台登录页
    await page.goto("https://signin.aliyun.com/login.htm#/main")
    # 切换到子账号登录TAB
    await expect(page.get_by_role("tab", name="RAM 用户名密码登录").locator("div")).to_be_visible()
    await page.get_by_role("tab", name="RAM 用户名密码登录").locator("div").click()
    await expect(page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>")).to_be_visible()
    # 清空账号框内容
    await page.get_by_role("grid").locator("i").first.click()
    await page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>").click()
    await page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>").fill(username)
    await page.get_by_role("button", name="下一步").click()
    # 清空密码框内容
    await page.get_by_role("grid").locator("i").nth(2).click()
    await page.locator("#loginPassword").click()
    await page.locator("#loginPassword").fill(password)
    # 点击登录按钮
    await page.get_by_role("button", name="登录").click()
    # 登录等待1.5秒请求完毕
    await page.wait_for_timeout(1000 * 1.5)
    # 重定向到dms页面
    await page.goto("https://dms.aliyun.com")
    print("=== DMS 登录完成 ===")
    await page.wait_for_timeout(timeout)
    # ---------------------
    await page.close()
    await context.close()
    await browser.close()


async def task() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


def start():
    try:
        if not username:
            print("username 缺失")
            sys.exit(1)

        if not password:
            print("password 缺失")
            sys.exit(1)

        if not timeout:
            print("timeout 缺失")
            sys.exit(1)
        asyncio.run(task())
    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print("控制台主动关闭")
    print('=== 浏览器已关闭 ===')


if __name__ == '__main__':
    start()
