# coding=utf-8
# date=2021/07

import xlrd
import re
import pandas as pd

f0='IMDB Dataset.xls'

ex=xlrd.open_workbook(filename=f0)
sheet = ex.sheet_by_name('IMDB Dataset')
cols=sheet.col_values(0)

lines=[]
for i in range(1,len(cols)):
    line=cols[i]
    p = "[^0-9A-Za-z\。\.\,\，\!\！\?\？' ']"     #使用正则表达式，只保留英文、数字、单词间空格、4类标点符号
    line=re.sub(p,"",line)
    lines.append(line)

line = pd.DataFrame(lines)
writer = pd.ExcelWriter('IMDB_after_pre.xls')# 写入Excel文件
line.to_excel(writer)
writer.save()
writer.close()