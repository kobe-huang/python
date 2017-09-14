# -*- coding: utf-8 -*- 
import xlrd
from collections import OrderedDict
import json
import codecs

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
  except Exception,e:
    print str(e)


# my_file = 'D:\kobe_doc\code\github\python\excel_demo\position_v0.1.xlsx';
# my_out_file = "D:\\kobe_doc\\code\\github\\python\\excel_demo\\gps_data.lua";
my_file = "D:\\kobe_doc\\code\\github\\python\\excel_demo\\111111.xlsx";
my_out_file = "D:\\kobe_doc\\code\\github\\python\\excel_demo\\my_data.lua";
const_pre_fix_city_str = "_city_info_";

def kobe_trans_excel_file_2_lua_table(excel_path):
    with codecs.open(my_out_file,"w","utf-8") as f:
          f.write("\n\n\n");

    workbook = xlrd.open_workbook(excel_path);
  #得到excel的第一页的数据
  #workbook = xlrd.open_workbook(r'F:\demo.xlsx')
  # 获取所有sheet
    print workbook.sheet_names(); # [u'sheet1', u'sheet2']
    sheet_name = workbook.sheet_names()[0];
    #print sheet_name;    
    my_sheet_num = len(workbook.sheets())
    for xx in xrange(0,my_sheet_num):

    # 根据sheet索引或者名称获取sheet内容
      sheet1 = workbook.sheet_by_index(xx); # sheet索引从0开始
      my_cloum_num = sheet1.ncols;
      
     
      tmp_col_name1 = "xxxx";
      str_fix_name = const_pre_fix_city_str + tmp_col_name1 + " = { \n"; #设置
      print my_cloum_num;
      for x in xrange(0, my_cloum_num ):
          my_cols = sheet1.col_values(x) # 获取列内容
          print my_cols
          tmp_col_name = my_cols[0];
          str_fix_name = str_fix_name + "\n" + "  " + tmp_col_name + "= { \n" + "    "
          tmp_row_num = len(my_cols);
          print tmp_row_num;
          for y in xrange(0, tmp_row_num-2):
              if my_cols[2+y] != "":
                  if True == isinstance(my_cols[2+y],(int,str,float)) :
                      str_fix_name = str_fix_name + "\"" + FloatToString(my_cols[2+y])+ "\"" + ",\n" + "    ";
                  else:   
                      str_fix_name = str_fix_name + "\"" + my_cols[2+y] + "\""+ ",\n" + "    ";
          str_fix_name  =  str_fix_name + "},\n";
      str_fix_name = str_fix_name + "};\n\n\n"
      with codecs.open(my_out_file,"a","utf-8") as f:
          f.write(str_fix_name);  

kobe_trans_excel_file_2_lua_table(my_file);









































def trans_excel_file_2_lua_table(excel_path):
    with codecs.open(my_out_file,"w","utf-8") as f:
          f.write("\n\n\n");

    workbook = xlrd.open_workbook(excel_path);
  #得到excel的第一页的数据
  #workbook = xlrd.open_workbook(r'F:\demo.xlsx')
  # 获取所有sheet
    print workbook.sheet_names(); # [u'sheet1', u'sheet2']
    sheet_name = workbook.sheet_names()[0];
    #print sheet_name;    
    my_sheet_num = len(workbook.sheets())
    for xx in xrange(0,my_sheet_num):

    # 根据sheet索引或者名称获取sheet内容
      sheet1 = workbook.sheet_by_index(xx); # sheet索引从0开始
      my_cloum_num = sheet1.ncols;
      
      my_cols1      = sheet1.col_values(0);
      tmp_col_name1 = my_cols1[2];

      str_fix_name = const_pre_fix_city_str + tmp_col_name1 + " = { \n"; #设置
      print my_cloum_num;
      for x in xrange(0, my_cloum_num ):
          my_cols = sheet1.col_values(x) # 获取列内容
          print my_cols
          tmp_col_name = my_cols[0];
          str_fix_name = str_fix_name + "\n" + "  " + tmp_col_name + "= { \n" + "    "
          tmp_row_num = len(my_cols);
          print tmp_row_num;
          for y in xrange(0, tmp_row_num-2):
              if my_cols[2+y] != "":
                  if True == isinstance(my_cols[2+y],(int,str,float)) :
                      str_fix_name = str_fix_name + "\"" + FloatToString(my_cols[2+y])+ "\"" + ",\n" + "    ";
                  else:   
                      str_fix_name = str_fix_name + "\"" + my_cols[2+y] + "\""+ ",\n" + "    ";
          str_fix_name  =  str_fix_name + "},\n";
      str_fix_name = str_fix_name + "};\n\n\n"

      with codecs.open(my_out_file,"a","utf-8") as f:
          f.write(str_fix_name);        



#trans_excel_file_2_lua_table(my_file);    




#根据索引获取Excel表格中的数据  参数:file：Excel文件路径   colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
   data = open_excel(file)
   table = data.sheets()[by_index]
   nrows = table.nrows #行数
   ncols = table.ncols #列数
   colnames = table.row_values(colnameindex) #某一行数据
   list =[]
   for rownum in range(1,nrows):
     row = table.row_values(rownum)
     if row:
       app = {}
       for i in range(len(colnames)):
         app[colnames[i]] = row[i]
       list.append(app)
   return list

# -*- coding: utf-8 -*-
# import xlrd
# import xlwt
# from datetime import date,datetime
 
def read_excel():
  # 打开文件
  workbook = xlrd.open_workbook(r'F:\\demo.xlsx')
  # 获取所有sheet
  print workbook.sheet_names() # [u'sheet1', u'sheet2']
  sheet2_name = workbook.sheet_names()[1]
 
  # 根据sheet索引或者名称获取sheet内容
  sheet2 = workbook.sheet_by_index(1) # sheet索引从0开始
  sheet2 = workbook.sheet_by_name('sheet2')
 
  # sheet的名称，行数，列数
  print sheet2.name,sheet2.nrows,sheet2.ncols
 
  # 获取整行和整列的值（数组）
  rows = sheet2.row_values(3) # 获取第四行内容
  cols = sheet2.col_values(2) # 获取第三列内容
  print rows
  print cols
 
  # 获取单元格内容
  print sheet2.cell(1,0).value.encode('utf-8')
  print sheet2.cell_value(1,0).encode('utf-8')
  print sheet2.row(1)[0].value.encode('utf-8')
   
  # 获取单元格内容的数据类型
  print sheet2.cell(1,0).ctype
 

