#关于excel配置
import os



BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


FILE_NAME = "test_case1.xlsx"
FILE_PATH =os.path.join(BASE_DIR,'data',FILE_NAME)

#--------------template cookies dict-----------------
COOKIES_DICT = {

}
#---------------allure 报告---------------------


ALLURE_COMMAND= 'allure generate {from_json_path} -o {save_to_path} --clean'.format(
    from_json_path=os.path.join(BASE_DIR,'report','json_result'),
    save_to_path=os.path.join(BASE_DIR,'report','allure_result')
)

#-------------------邮件相关-----------------------------

MAIL_HOST=''
MAIL_USER='shuang.wu@fatritech.com'
MAIL_TOKEN=''
#设置收件人 和发件人
SENDER=''
RECEIVERS=['','']
#邮件主题
THEND='自动化测试报告'
#正文内容
SEND_CONTENT='HI,MAN,你收到邮件了吗<h1>用例失败数：{}</h1>'
#附件
SEND_FILE_NAME=os.path.join(BASE_DIR,'report','allure_report.zip')
