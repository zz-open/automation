# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-02-20 12:30:31
@describe 自动登录阿里云DMS管理平台
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, Any
import yaml
import asyncio
import click
from playwright.async_api import Playwright, async_playwright, expect

conf = {}
# stealth.min.js文件的存放路径
STEALTH_PATH = f"{os.getcwd()}/stealth.min.js"


async def run(playwright: Playwright) -> None:
    print("=== DMS LOGIN START ===")
    browser = await playwright.chromium.launch(headless=False, chromium_sandbox=False,
                                               ignore_default_args=["--enable-automation"],
                                               channel="chrome", args=['--start-maximized'])
    ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
          'Safari/537.36')
    context = await browser.new_context(user_agent=ua, no_viewport=True)
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
    await page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>").fill(conf.get("username"))
    await page.get_by_role("button", name="下一步").click()
    # 清空密码框内容
    await page.get_by_role("grid").locator("i").nth(2).click()
    await page.locator("#loginPassword").click()
    await page.locator("#loginPassword").fill(conf.get("password"))
    # 点击登录按钮
    await page.get_by_role("button", name="登录").click()
    # 登录等待1.5秒请求完毕
    await page.wait_for_timeout(1000 * 1.5)
    # 重定向到dms页面
    await page.goto("https://dms.aliyun.com")
    print("=== DMS LOGIN END ===")
    await page.wait_for_timeout(conf.get("timeout"))
    # ---------------------
    await page.close()
    await context.close()
    await browser.close()


async def task() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


def start():
    try:
        asyncio.run(task())
    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print("控制台主动关闭")
    print('=== 浏览器已关闭 ===')


def get_conf_abs_path(path_: str) -> str:
    if not path_:
        return ""
    if os.path.isabs(path_):
        return path_

    new_path = f'{os.path.dirname(__file__)}/{path_}'
    return os.path.abspath(new_path)


def parse_yaml(_path: str) -> Dict[str, Any]:
    if not _path:
        raise Exception("yaml path 不能为空")

    conf_path = get_conf_abs_path(_path)
    if not os.path.exists(conf_path):
        raise Exception(f"{conf_path} 不存在")

    with open(conf_path, 'r') as f:
        data = yaml.safe_load(f)
        return {} if data is None else data


@click.command()
@click.option("-f", "--file", type=str, default="./conf.yaml", required=False, help="yaml配置文件")
def command(file):
    if os.path.isabs(file):
        abs_file_path = file
    else:
        abs_file_path = os.path.abspath(f"{os.getcwd()}/{file}")

    click.echo(click.style(f"配置文件: {abs_file_path}", fg="red", bold=True))

    global conf
    conf = parse_yaml(abs_file_path)
    username = conf.get("username", "")
    password = conf.get("password", "")
    timeout = conf.get("timeout", 1000 * 60 * 60 * 24)
    if not username:
        print("username 缺失")
        sys.exit(1)

    if not password:
        print("password 缺失")
        sys.exit(1)

    if not timeout:
        print("timeout 缺失")
        sys.exit(1)

    conf["username"] = username
    conf["password"] = password
    conf["timeout"] = timeout
    start()


if __name__ == '__main__':
    command()
