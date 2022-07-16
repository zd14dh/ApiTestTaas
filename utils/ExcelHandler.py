'''
专门处理Excel
'''
import xlrd
from conf import settings
import jsonpath_rw



#获取所有行和列
# print(sheet.nrows,sheet.ncols)

#获取第一行的数据
# print(sheet.row_values(0))
# print(sheet.row_values(1))

#获取指定列
# print(sheet.col_values(0))

class ExcelOperate(object):
    def __init__(self,file_path,sheet_by_index=0):
        self.file_path=file_path
        self.sheet_by_index=sheet_by_index
        #打开对象文件
        book = xlrd.open_workbook(self.file_path)
        #读取sheet文件
        self.sheet = book.sheet_by_index(self.sheet_by_index)

    def get_excel(self):
        l = []
        #第一行是头
        title=self.sheet.row_values(0)
        print(title)
        # for row in range(1,self.sheet.nrows):
        #     roo=self.sheet.row_values(row)
        #     # print(sheet.row_values(row))
        #     l.append(dict(zip(title,roo)))
        return [dict(zip(title,self.sheet.row_values(row))) for row in range(1,self.sheet.nrows)]

if __name__ == '__main__':
    list=ExcelOperate(settings.FILE_PATH,0).get_excel()
    print(list)
    # for item in list:
    #     print('+++++++++',item)