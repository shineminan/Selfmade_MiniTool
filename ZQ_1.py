import pandas as pd
import numpy as np

xls = pd.ExcelFile("C:\\Users\\shine\\Desktop\\ZQ.xlsx")
sheet1 = pd.read_excel(xls, 'Sheet1')
sheet2 = pd.read_excel(xls, 'Sheet2')


sheet1_Nr = list(sheet1["父订单号"])
sheet2_Nr = list(sheet2["主订单号"])

samenumberlst = []
for nr in sheet2_Nr:
    if nr in sheet1_Nr:
        samenumberlst.append(nr)

print(samenumberlst)