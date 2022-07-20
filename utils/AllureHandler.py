'''
allure报告相关
'''
import os
import time
import win32com.client as win32
from subprocess import Popen,call
from conf import settings
from conf.settings import ALLURE_COMMAND

class AllureOperate(object):

    def get_allure_report(self,filed):
        '''生成报告'''
        # os.system(ALLURE_COMMAND)
        call(ALLURE_COMMAND,shell=True)

        # self.check_zip()

        # self.send_mail(filed)
    def check_zip(self):
        '''打包'''
        import zipfile
        #BASE_DIR:当前脚本的父级目录
        BASE_DIR =os.path.join(settings.BASE_DIR,'report')
        start_zip_dir=os.path.join(BASE_DIR,'allure_result') #压缩文件的根目录
        zip_file_name='allure_report.zip'#压缩后的文件名称

        zip_file_path=os.path.join(BASE_DIR,zip_file_name)
        f = zipfile.ZipFile(zip_file_path,'w',zipfile.ZIP_DEFLATED)
        for dir_path,dir_name,file_names in os.walk(start_zip_dir):
            #要是不replace，就从根目录开始复制
            file_path=dir_path.replace(start_zip_dir,'')
            #实现当前文件夹以及包含的所有文件
            file_path =file_path and file_path +os.sep or ''
            for file_name in file_names:
                f.write(os.path.join(dir_path,file_name),file_path+file_name)
        f.close()





    def send_mail(self,filed):
        '''发邮件'''
        outlook = win32.Dispatch('Outlook.Application')

        mail_item = outlook.CreateItem(0)  # 0:olMailItem
        mailist = [settings.MAIL_USER]

        for i in range(len(mailist)):
            mail_item.Recipients.Add(mailist[i])
            mail_item.Subject = settings.THEND

            mail_item.BodyFormat = 2  # 2:Htmlformat
            mail_item.HTMLBody = '<h1>用例错误有：{}</h1>'.format(filed)
            mail_item.Attachments.Add(settings.SEND_FILE_NAME)
            mail_item.Send()


# if __name__ == '__main__':
#     AllureOperate().get_allure_report()