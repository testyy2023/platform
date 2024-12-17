import os
from common.clear_folder import clean_files
import common.clear_folder
import pytest
import allure_pytest

deletelist=("screenshot","download_files","allure_report")
for testfiles in deletelist:
    print(testfiles)
    clean_files(testfiles)
    print("{}删除成功".format(testfiles))

pytest.main(["-s","--headed","--html=../report/report.html","--clean-alluredir","--alluredir=./allure_results"])
#将allure的执行数据生成allure可视化报告
os.system(r"allure generate ./allure_results -o ./allure_report --clean")
# 打开allure临时报告
os.system("allure open ./allure_report")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/