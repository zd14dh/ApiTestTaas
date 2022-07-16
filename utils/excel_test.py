
import os
from conf import settings
import xlrd



class ExcelTest():
    def __init__(self,execl_path,sheet_by_index=0):
        self.execl_path=execl_path
        self.sheet_by_index=sheet_by_index
        book=xlrd.open_workbook(self.execl_path)
        self.sheet=book.sheet_by_index(self.sheet_by_index)

    def get_excel(self):
        l=[]
        title=self.sheet.row_values(0)

        # for row in range(1,self.sheet.nrows):
        #
        #     nrow=self.sheet.row_values(row)
        #     l.append(dict(zip(title,nrow)))

        print([dict(zip(title,self.sheet.row_values(row)))  for row in range(1,self.sheet.nrows)])

if __name__ == '__main__':
    FILE_PATH=os.path.join(os.path.abspath(os.pardir),'data','test_case1.xlsx')
    print(FILE_PATH)
    execl=ExcelTest(FILE_PATH,0).get_excel()