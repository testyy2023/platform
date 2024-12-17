import os
import time
import pytest
from playwright.sync_api import Page, expect
from common import test_login


@pytest.mark.run(order=1)
def test_tpmcreate(page: Page,set_global_data) -> None:
    test_login.userlogin(page, "shanghai", "1")
    page.wait_for_selector("#leftMenuId_DOC_MODULE > span")
    page.click("#leftMenuId_DOC_MODULE > span")
    page.get_by_text("报告管理").click()
    page.get_by_text("报告模板").click()
    page.get_by_role("button", name="创 建").click()
    page.get_by_label("创建模板").locator("input[type=\"text\"]").click()
    tmp_title = "回归测试-模板创建"+time.strftime("%Y%m%d%H%M%S")
    print(tmp_title)
    page.get_by_label("创建模板").locator("input[type=\"text\"]").fill(tmp_title)
    page.get_by_label("创建模板").locator("textarea").click()
    page.get_by_label("创建模板").locator("textarea").fill("回归测试-模板描述添加1143")
    page.locator("#rc_select_15").click()
    page.get_by_text("日度").nth(1).click()
    page.locator("#rc_select_16").click()
    page.get_by_role("tree").get_by_title("财产险").click()
    page.locator("#rc_select_17").click()
    page.get_by_role("tree").get_by_text("零售金融").click()
    page.get_by_role("button", name="确 定").click()
    with page.expect_file_chooser() as fc_info:
        page.locator("#file").get_by_role("button").click()
    file_chooser = fc_info.value
    file_chooser.set_files("../upload_files/中银保险有限公司2024年一季度全面风险报告 - 副本.docx")
    # page.locator("#file").get_by_role("button").set_input_files("中银保险有限公司2024年一季度全面风险报告 - 副本.docx")
    time.sleep(1)
    page.get_by_role("button", name="确 定").click()
    time.sleep(2)
    page.screenshot(path="../screenshot/tmpcreate{}.png".format(time.strftime("%Y%m%d%H%M%S")))
    # time.sleep(2)
    expect(page.get_by_text("创建成功")).to_be_visible()
    time.sleep(2)
    print("模板创建成功{}".format(tmp_title))
    set_global_data("tmp_title",tmp_title)
    # return tmp_title

@pytest.mark.run(order=2)
def test_version(page: Page,get_global_data) -> None:
    test_login.userlogin(page, "shanghai", "1")
    page.locator("#leftMenuId_DOC_MODULE").get_by_text("报告管理").click()
    tmp_title= get_global_data("tmp_title")
    page.get_by_text("报告模板").click()
    page.get_by_placeholder("请填写模板名称").click()
    page.get_by_placeholder("请填写模板名称").fill(tmp_title)
    # page.get_by_placeholder("请填写模板名称").fill(t)
    page.get_by_role("button", name="查 询").click()
    page.get_by_role("button", name="版本").click()
    page.get_by_role("button", name="复制").click()
    page.get_by_text("确认", exact=True).click()
    expect(page.get_by_text("复制成功")).to_be_visible()
    print("版本复制功能正确")
    with page.expect_download() as download_info:
        page.get_by_role("gridcell", name="删除 下载 复制").locator("#download").click()
    download = download_info.value
    download.save_as("../download_files/"+download.suggested_filename)
    if os.path.isfile("../download_files/{}".format(download.suggested_filename)):
        print("版本下载功能正确")
    page.get_by_role("button", name="删除").click()
    page.get_by_text("确认", exact=True).click()
    expect(page.get_by_text("删除成功")).to_be_visible()
    print("版本删除功能正确")

@pytest.mark.run(order=3)
def test_tmpdelete(page: Page,get_global_data) -> None:
    test_login.userlogin(page, "shanghai", "1")
    page.wait_for_selector("#leftMenuId_DOC_MODULE > span")
    page.click("#leftMenuId_DOC_MODULE > span")
    page.get_by_text("报告管理").click()
    page.get_by_text("报告模板").click()
    tmp_title = get_global_data("tmp_title")
    page.get_by_placeholder("请填写模板名称").click()
    page.get_by_placeholder("请填写模板名称").fill(tmp_title)
    page.get_by_role("button", name="查 询").click()
    page.locator("div:nth-child(2) > .ag-new > .ag-theme-alpine > div > div > .ag-root-wrapper > .ag-root-wrapper-body > .ag-root > .ag-body-viewport > .ag-pinned-left-cols-container > .ag-row-even > div > .ag-cell-wrapper > .ag-selection-checkbox").click()
    page.get_by_role("button", name="删 除").click()
    page.get_by_text("确认", exact=True).click()
    print("报告模板删除成功")
