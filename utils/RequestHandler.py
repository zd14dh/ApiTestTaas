import re
import json
import requests
from conf import settings
from jsonpath_rw import parse
from urllib.parse import urlparse
from utils.ExcelHandler import ExcelOperate

#--------------有数据依赖的写法-------------------



#---------------没有依赖的写法--------------------------
class RequestOperate(object):

    def __init__(self,current_case,all_excel_data_list):
        self.current_case=current_case
        self.all_excel_data_list=all_excel_data_list

    def get_response_msg(self):
        """发送请求并且获取结果"""
        return self._send_msg()


    def _send_msg(self):
        """发请求"""
        # print(111111111111111,self.current_case)
        response=requests.request(
            method=self.current_case['method'],
            url=self.current_case['url'],
            data=self._check__request_data(),
            params=self._check__request_params(),
            cookies=self._check__request_cookies(),
            json=self._check__request_json(),
            headers=self._check__request_headers()
        )
        # print("{}==============请求结果============".format(self.current_case['case_num']),response.json(),'==================')
        self._write_cookies(response)
        # json.loads(self.current_case['except'])
        # print(type(self.current_case['except']),self.current_case['except'],response.json())
        return json.loads(self.current_case['except']),response.json()

    def _write_cookies(self,response):
        '''监测响应结果是否含有cookies，有就保存起来'''
        cookies=response.cookies.get_dict()
        for item in self.all_excel_data_list:
            if item['case_num']==self.current_case['case_num']:
                item['temporary_response_cookies']=response.cookies.get_dict()
                item['temporary_response_json']=response.json()



    def _check__request_cookies(self):
        '''处理请求中的cookies'''


    def _write_token(self,response):
        for item in self.all_excel_data_list:
            if item['case_num']==self.current_case['case_num']:
                if response.headers['Content-Type'].lower()=='application/json':
                    item['temporary_response_json']=response.json()
                item['temporary_request_headers']=self.current_case['headers']
                item['temporary_request_data']=self.current_case['data']
                item['temporary_request_json']=self.current_case['json']
                item['temporary_request_params']=self.current_case['params']
                item['temporary_response_headers']=response['headers']



    def _check__request_json(self):
        json1=self.current_case['json']
        if json1:
            return json.loads(json1)
        else:
            return {}



    def _check__request_data(self):
        """处理请求的params参数，检查是否有依赖"""
        data =self.current_case['data']
        if data:
            return json.dumps(data)
        else:
            return {}

    def _check__request_params(self):
        """处理请求的data参数，检查是否有依赖"""
        params =self.current_case['params']
        if params:
            pass
        else:
            return {}

    def _check__request_headers(self):
        headers=self.current_case.get("headers",None)
        if headers:
            return self._optrate_re_mag(headers)
        else:
            return {}

    def _optrate_re_mag(self,parameter):
        """
        正则校验，数据依赖的字段
        :param parameter: 各种参数，如：data，headers
        :return:
        """
        # print(2222222222,parameter)
        if isinstance(parameter,dict):
            parameter =json.dumps(parameter)
        pattern=re.compile('\${(.*?)}\$')
        rule_list=pattern.findall(parameter)

        # print(3333333333333,parameter)
        if rule_list:#该参数有数据依赖，要处理
            for rule in rule_list:
                case_num,params,json_path=rule.split(">")
                # print(case_num,params,json_path)
                for line in self.all_excel_data_list:
                    if line['case_num']==case_num:
                        temp_data=line["temporary_{}".format(params)]
                        # print(type(temp_data),temp_data)
                        if isinstance(temp_data,str):
                            temp_data=json.loads(temp_data)
                        match_list=parse(json_path).find(temp_data)
                        if match_list:
                            match_data=[v.value for v in match_list][0]
                            # print(match_data)
                        #将提取出来的值替换到原来的规则
                            parameter=re.sub(pattern=pattern,repl=match_data,string=parameter,count=1)
                # print(444444444,parameter,type(parameter))
                return json.loads(parameter)
        else:
            print(parameter)
            if isinstance(parameter,str):
                parameter=json.loads(parameter)
                return parameter


if __name__ == '__main__':

    excel_list=ExcelOperate(settings.FILE_PATH,0).get_excel()

    for item in excel_list:
        RequestOperate(current_case=item,all_excel_data_list=excel_list).get_response_msg()
