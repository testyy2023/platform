import time

import pytest
from playwright.sync_api import Page, expect

def userlogin(page: Page,useId,password):
    page.goto("http://192.168.252.91:8083/xweb-document/micro/doc/")
    page.goto("http://192.168.252.91:8083/xweb-document/micro/doc/#/")
    page.goto("http://192.168.252.91:8083/xweb-document/micro/doc/#/welcome")
    page.goto("http://192.168.252.91:8083/xweb-document/micro/doc/#/user/login")
    page.get_by_placeholder("用户名").click()
    page.get_by_placeholder("用户名").fill(useId)
    page.get_by_placeholder("用户名").press("Tab")
    page.get_by_placeholder("密码").fill(password)
    page.get_by_role("button", name="登 录").click()
    page.wait_for_selector("body > div:nth-child(5) > div > div > div > div > div > span:nth-child(2)").is_visible()
    if page.get_by_text("登录成功!").is_visible():
        login_status = "登录成功"
    else:
        page.screenshot(path="../screenshot/loginerror{}.png".format(time.strftime("%Y%m%d%H%M%S")))
        login_status = "登录失败"

    return login_status