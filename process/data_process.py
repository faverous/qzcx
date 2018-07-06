# --coding:utf-8--
'''
将原始数据进行整理，保留所需数据并生成excel文件
'''

import numpy as np
import xlrd
import xlsxwriter
import xlwt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


def in_excel(inpath, x):
    print("----开始读取excel数据----")
    ori_data = xlrd.open_workbook(inpath)
    print('123')
    table = ori_data.sheets()[x]  #获取第x张工作表
    rows_start = 389  #起始行
    rows_end = table.nrows  #结束行
    col_start = 0  #起始列
    col_end = table.ncols  #结束列
    output = []  #输出列表
    num = 0  #计数
    for i in range(rows_start, rows_end):
        values = []
        row = table.row_values(i)
        if row[2] and row[3]:
            for j in range(col_start, col_end):
                if (not row[j] and num > 0):
                    values.append(output[num - 1][j])
                else:
                    values.append(row[j])
            output.append(values)
            num = num + 1
    print("----读取完成---- ")
    return output


def out_excel(tmplist, outpath):
    print("----开始写入数据----")
    pos_data = xlsxwriter.Workbook(outpath)
    worksheet = pos_data.add_worksheet()
    # style = xlwt.XFStyle()
    # style.num_format_str = "[$-10804]0.00"
    rows_pos = len(tmplist)
    col_pos = len(tmplist[0])
    print(rows_pos)
    for i in range(rows_pos):
        for j in range(col_pos):
            worksheet.write(i, j, tmplist[i][j])
        worksheet.write(i, j, tmplist[i][j])
    pos_data.close()
    print("----写入完成----")


'''通用读取文件，返回列表'''


def input_com(inpath, i):
    data = xlrd.open_workbook(inpath)
    table = data.sheets()[i]  #获取第x张工作表
    rows = table.nrows
    cols = table.ncols
    output = []
    for i in range(1, rows):
        values = []
        row = table.row_values(i)
        for j in range(cols):
            values.append(row[j])
        output.append(values)
    return output


'''规范化方法1'''


def max_min(inpath, i):
    print("----开始规范化----")
    output = input_com(inpath, i)
    arr = np.array(output)
    arr_new = MinMaxScaler().fit_transform(arr)
    # arr = np.array(output).T
    # del_list = []
    # min_list = []
    # for i in range(len(arr)):
    #     maxtmp = np.max(arr[i])
    #     mintmp = np.min(arr[i])
    #     del_list.append(maxtmp - mintmp)
    #     min_list.append(mintmp)
    # for i in range(len(output)):
    #     for j in range(len(output[0])):
    #         if(del_list[j]==0):
    #             output[i][j] = 0
    #         else:
    #             output[i][j] = (output[i][j] - min_list[j]) / del_list[j]
    print("----规范化完成----")
    return arr_new


'''规范化方法2'''


def z_score(inpath, i):
    output = input_com(inpath, i)
    arr = np.array(output)
    arr_new = StandardScaler().fit_transform(arr)
    return arr_new


if __name__ == '__main__':
    inpath = "sz_original_all.xls"
    # outpath = "pos_data2.xlsx"
    # output = in_excel(inpath,0)
    # out_excel(output,outpath)
    arr = in_excel(inpath, 1)
    out_excel(arr, "sz_pos_all1.xlsx")
