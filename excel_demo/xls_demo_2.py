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
my_file = "D:\\kobe_doc\\code\\github\\python\\excel_demo\\wx_phone_num.xlsx";
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
                  if True == isinstance(my_cols[2+y],(float)) :
                      tmp_string =  FloatToString(my_cols[2+y]);
                      if 11 != len(tmp_string) : 
                        continue;
                      str_fix_name = str_fix_name + "\"" + FloatToString(my_cols[2+y])+ "\"" + ",\n" + "    ";                      
                  else:
                      if 11 != len(my_cols[2+y]) : 
                        continue;   
                      str_fix_name = str_fix_name + "\"" + my_cols[2+y] + "\""+ ",\n" + "    ";
                     
          str_fix_name  =  str_fix_name + "},\n";
      str_fix_name = str_fix_name + "};\n\n\n"
      with codecs.open(my_out_file,"a","utf-8") as f:
          f.write(str_fix_name);  

kobe_trans_excel_file_2_lua_table(my_file);