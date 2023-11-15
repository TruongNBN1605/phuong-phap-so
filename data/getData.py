import os
import openpyxl

def getDataFromExcel(fileName, filePath):
    absolutePath =  os.path.abspath(f'{filePath}{fileName}.xlsx')
    wb = openpyxl.load_workbook(absolutePath) 
    sheet = wb.active

    x = None
    xValues = []
    yValues = []

    fistRow = True
    for row in sheet.iter_rows(values_only=True):
        if fistRow:
            x = row[1]
            fistRow = False
            continue  
        else:
            xValues.append(row[0])
            yValues.append(row[1])
    # In ra hai mảng
    return xValues, yValues, x
