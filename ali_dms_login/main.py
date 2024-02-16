# -*- coding: utf-8 -*-

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://signin.aliyun.com/login.htm#/main")
    # page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>").click()
    # page.get_by_role("grid").locator("i").first.click()
    # page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>").click()
    # page.get_by_placeholder("<用户名>@<默认域名> 或 <用户名>@<企业别名>").fill("gsu_developer@1750722755809809")
    # page.get_by_role("button", name="下一步").click()
    # page.get_by_role("grid").locator("i").nth(2).click()
    # page.locator("#loginPassword").click()
    # page.locator("#loginPassword").fill("rdsrw@dev-gSu1")
    # page.get_by_role("button", name="登录").click()
    # page.goto("https://dms.console.aliyun.com/#/dms/login")
    # page.get_by_role("button", name="登录").click()
    # page.get_by_text("SQL窗口", exact=True).click()

    # input("-----等待关闭----")
    # ---------------------
    context.close()
    browser.close()


def main():
    with sync_playwright() as playwright:
        run(playwright)
    print('===执行结束===')


if __name__ == '__main__':
    main()
