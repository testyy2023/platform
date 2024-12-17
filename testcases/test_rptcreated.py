import re
import time

from playwright.sync_api import Page, expect


def test_reportcreated(page: Page) -> None:
    page.goto("http://192.168.252.91:8083/xweb-document/micro/doc/#/user/login")
    page.get_by_placeholder("用户名").click()
    page.get_by_placeholder("用户名").fill("9999")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("123")
    page.get_by_role("button", name="登 录").click()
    page.wait_for_selector("#leftMenuId_DOC_MODULE > span")
    page.click("#leftMenuId_DOC_MODULE > span")
    page.get_by_text("报告管理").nth(2).click()
    page.get_by_role("button", name="创 建").click()
    page.get_by_role("switch").click()
    page.locator("#rc_select_18").click()
    page.get_by_title("月度").locator("div").click()
    page.get_by_placeholder("请选择月份").click()
    page.get_by_text("1月", exact=True).click()
    page.locator("#auditPeriodValue > div > .XSelect___u8-6h > .ant-select > .ant-select-selector > .ant-select-selection-item").click()
    page.get_by_title("13期").locator("div").click()
    page.locator("#entityTypeName span").nth(1).click()
    page.get_by_title("单位").locator("div").click()
    page.locator("#entityName span").nth(1).click()
    page.get_by_title("普联软件").locator("div").click()
    page.locator(".XTreeSelect___1IcK0 > .ant-select > .ant-select-selector > .ant-select-selection-item").first.click()
    page.get_by_title("市场风险").locator("span").click()
    page.locator("#categoryList_C_DOC_CATEGORY_TYPE > div > .XTreeSelect___1IcK0 > .ant-select > .ant-select-selector > .ant-select-selection-item").click()
    page.get_by_title("零售金融").locator("span").click()
    page.get_by_label("创建报告").locator("input[type=\"text\"]").click()
    page.get_by_label("创建报告").locator("input[type=\"text\"]").fill("2024年1月测试平台报告")
    page.get_by_label("创建报告").locator("textarea").click()
    page.get_by_label("创建报告").locator("textarea").fill("报告摘要描述")
    with page.expect_file_chooser() as fc_info:
        page.locator("button").filter(has_text="报告文件").click()
    file_chooser = fc_info.value
    file_chooser.set_files("../upload_files/中银保险有限公司2024年一季度全面风险报告 - 副本.docx")
    time.sleep(1)
    page.get_by_role("button", name="确 定").click()
    time.sleep(3)
    expect(page.get_by_text("创建成功")).to_be_visible()