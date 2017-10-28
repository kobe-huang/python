# -*- coding: utf-8 -*- 
import xlrd
from collections import OrderedDict
import json
import codecs
import time 
from time import strftime,gmtime
from datetime import datetime

# import importlib,sys
# importlib.reload(sys)

# my_file     = sys.path[0] + "\\xx\\xx_page_info.xlsx";
# my_out_file = sys.path[0] + "\\xx\\sl_func__xx_page_info.lua";
# 
# my_file     = sys.path[0] + "\\hs\\hs_page_info.xlsx";
# my_out_file = sys.path[0] + "\\hs\\sl_func__hs_page_info.lua";


def FloatToString (aFloat):
    if type(aFloat) != float:
        return ""
    strTemp = str(aFloat)
    strList = strTemp.split(".")
    if len(strList) == 1 :
        return strTemp
    else:
        if strList[1] == "0" :
            return strList[0]
        else:
            return strTemp


def open_excel(file):
  try:
    data = xlrd.open_workbook(file)
    return data
  except Exception as e:
    print (str(e))
    return False;


#根据索引获取Excel表格中的数据  参数:file：Excel文件路径   colnameindex：表头列名所在行的所以 ，by_index：表的索引
# def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
def excel_table_by_index(file, colnameindex=0, by_index=0):
    data  = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames = table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(2,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def excel_table_by_index_2(file, colnameindex=0, by_index=0):
    data  = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames = table.row_values(colnameindex) #某一行数据
    list ={}
    for colnum in range(0, ncols):
        if "" != colnames[colnum]:
            col = table.col_values(colnum)  #读取某一列的值
            if col:
                app = []
                for i in range(2, len(col)):
                    if "" != col[i]:
                        app.append(col[i])
                list[colnames[colnum]] = tuple(app)
                print(colnames[colnum]);
    return list



def analysis_row_data(input_dict):
    print(input_dict["name_en"]);
    if input_dict["info"] == "" :
        return do_point_info(input_dict);
    else:
        return do_shot_info(input_dict);


def trans_excel_file_2_table(file):
    list = excel_table_by_index(file, );
    print(len(list));
    #time_str = strftime("%Y-%m-%d %H:%M:%S", gmtime());
    time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    with codecs.open(my_out_file,"w","utf-8") as f:
        f.write("-----"+time_str + "\n\n");
        for x in xrange(0,len(list)):
            my_str = analysis_row_data(list[x]);
            if "" != my_str :
                f.write(my_str);
        f.close();
