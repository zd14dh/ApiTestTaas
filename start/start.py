import pytest
import shutil
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf.settings import BASE_DIR
from utils.AllureHandler import AllureOperate



if __name__ == '__main__':
    # 删除之前的json文件
    dir_path = os.path.join(BASE_DIR, 'report', 'json_result')
    # # BASE_DIR2=os.path.dirname(os.getcwd())
    # ---递归删除目录，无法直接删除文件-----
    shutil.rmtree(dir_path)
    # 更改工作目录
    os.chdir(BASE_DIR)
    # 执行用例
    pyvalue=pytest.main().value

    # 生成allure报告
    AllureOperate().get_allure_report(pyvalue)
