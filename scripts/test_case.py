import os
import allure
import pytest

from conf import settings
from deepdiff import DeepDiff
from utils.ExcelHandler import ExcelOperate
from utils.RequestHandler import RequestOperate

from conf import settings

excel_list= ExcelOperate(settings.FILE_PATH,0).get_excel()


class TestCase(object):
    @pytest.mark.parametrize('item',excel_list)
    def test_case(self,item):
        except_data,result=RequestOperate(current_case=item,all_excel_data_list=excel_list).get_response_msg()
        allure.dynamic.title(item['title'])
        # print(DeepDiff(except_data,result))
        assert not DeepDiff(except_data,result).get('values_changed',None)


# def setup_module():
#     os.remove(os.path.join(settings.BASE_DIR,'report','json_result'))


# if __name__ == '__main__':

    # print('错误用例：',pytest.main().value)
    # print('执行用例：',pytest.main())
