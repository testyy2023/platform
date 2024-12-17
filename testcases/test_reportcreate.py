import time

import allure
import pytest
from common import test_login
from playwright.sync_api import Page, expect
@pytest.mark.skip("")
@pytest.mark.run(order=1)
@allure.step("报告创建")
def test_reportcreate(page: Page) -> None:
        login_status = test_login.userlogin(page, "shanghai", "1")
        print(login_status)
        page.wait_for_selector("#leftMenuId_DOC_MODULE > span")
        page.click("#leftMenuId_DOC_MODULE > span")
        page.get_by_text("报告管理").nth(2).click()
        page.get_by_role("button", name="创 建").click()
        page.locator("#rc_select_14").click()
        page.locator("#rc_select_14").fill("回归")
        page.get_by_text("回归测试-模板创建", exact=True).click()
        page.get_by_placeholder("请选择月份").click()
        page.get_by_text("1月", exact=True).click()
        page.get_by_label("创建报告").locator("textarea").click()
        page.get_by_label("创建报告").locator("textarea").fill("报告描述回归测试记录")
        page.get_by_role("button", name="确 定").click()
        page.screenshot(path="../screenshot/rptcreateerror{}.png".format(time.strftime("%Y%m%d%H%M%S")))
        expect(page.get_by_text("创建成功")).to_be_visible()
        print("报告创建成功")


@pytest.mark.run(order=2)
def test_reportdelete(page: Page) -> None:
    test_login.userlogin(page, "shanghai", "1")
    page.wait_for_selector("#leftMenuId_DOC_MODULE > span")
    page.click("#leftMenuId_DOC_MODULE > span")
    page.get_by_text("报告管理").nth(2).click()
    page.get_by_placeholder("请填写报告名称").click()
    page.get_by_placeholder("请填写报告名称").fill("回归测试")
    page.get_by_role("button", name="查 询").click()
    # page.wait_for_selector("Press Space to toggle row")
    page.locator(".ag-selection-checkbox").click()
    page.get_by_role("button", name="删 除").click()
    page.get_by_text("确认", exact=True).click()
    expect(page.get_by_text("删除成功")).to_be_visible()
    print("报告删除成功")
