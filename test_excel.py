import xlrd

file_path = "/Users/shubham/Documents/work/TrainWithShubham/Python-Tuts/sqlite/test.xlsx"

book = xlrd.open_workbook(file_path)

sheet = book.sheet_by_index(0)
for i in range(sheet.ncols):
    name = sheet.cell_value(1, i)


    