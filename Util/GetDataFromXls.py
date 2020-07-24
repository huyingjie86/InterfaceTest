import json
import xlrd
import xlutils


class GetDataFromXls:
    # 读取excel值
    excelDir = r'..\file\interface _test_case.xlsx'
    # 打开excel
    workbook = xlrd.open_workbook(excelDir)
    # print(workbook.sheet_names())
    # worksheet = workbook.sheet_by_name()[1]
    worksheet = workbook.sheet_by_name('Sheet1')

    # 读取一行
    def getDataByRow(self, num):
        rows = GetDataFromXls.worksheet.row_values(num)
        # print(rows)
        return rows

    # 读取一列
    def getDataByClo(self, num):
        clo = GetDataFromXls.worksheet.col_values(num)
        # print(clo)
        return clo

    # 读取单元格
    def getDataByCellData(self, row, clo):
        cellData = GetDataFromXls.worksheet.cell_value(row, clo)
        # print(cellData)
        return cellData
        # print(worksheet.cell(1, 6).ctype)  # 单元格数据类型 0 1：string 2 3 4 5

    # 读取excel中所有数据
    def getAllData(self):
        allData = []
        for row in range(1, GetDataFromXls.worksheet.nrows):
            data = GetDataFromXls.worksheet.row_values(row)
            allData.append(data)
        return allData

