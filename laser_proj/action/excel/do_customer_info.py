# -*- coding: utf-8 -*- 
import xlrd
import xlwt

from collections import OrderedDict
import json
import codecs
import time 
from time import strftime,gmtime
from datetime import datetime


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


#---------------------------------------------------------------------
def set_style(name,height,bold=False):
    style = xlwt.XFStyle() # 初始化样式

    font = xlwt.Font() # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

 
#写excel
def write_excel(save_path, save_contain):
    f = xlwt.Workbook() #创建工作簿
    '''
    创建第一个sheet:
    sheet1
    '''
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    row0 = ["序号","客户","项目","操作员","时间","内容"]

    for i in range(0,len(row0)):
        sheet1.write(0, i, row0[i], set_style('微软雅黑',220,True))

    for i in range(len(save_contain)):  
        for m in range(len(save_contain[i])):
            sheet1.write(i+1, m, save_contain[i][m], set_style('微软雅黑',220,False))    
    f.save(save_path) #保存文件