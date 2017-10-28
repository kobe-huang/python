# -*- coding: utf-8 -*- 
import xlrd
from collections import OrderedDict
import json
import codecs
import sys
reload(sys)  
sys.setdefaultencoding('utf8')  

my_file     = sys.path[0] + "\\xx_page_info.xlsx";
my_out_file = sys.path[0] + "\\my_data.lua";


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

   


def do_point_info(input_dict):
    my_list  =  input_dict["position"].split(";")
    full_str = "\n" + "---点：" + input_dict["name_cn"] +"\n"
    full_str = full_str + "init_point{name = ";
    full_str = full_str + "\"" + input_dict["name_en"] + "_p\",  ";
    full_str = full_str + "x = " + str(my_list[0]) + ", "
    full_str = full_str + "y = " + str(my_list[1]) + " "
    full_str = full_str + " }\n"
    return full_str


############################
def do_shot_info(input_dict):
    my_list  =  input_dict["position"].split(";")
    full_str = "\n" + "---图像：" + input_dict["name_cn"] +"\n"
    full_str = full_str + input_dict["name_en"] + "_info = {\n"
    full_str = full_str + "    compare_info = {"
    full_str = full_str + input_dict["info"].strip('\n') + "},\n"

    full_str = full_str + "    rate = "     + '%d' %input_dict["degree"] +",\n"
    full_str = full_str + "    start_x = "  + str(my_list[0]) + ", "
    full_str = full_str + "start_y = "  + str(my_list[1]) + ", "
    full_str = full_str + "end_x = "    + str(my_list[2]) + ", "
    full_str = full_str + "end_y = "    + str(my_list[3]) + ", \n"
    full_str = full_str + "}\n"

    #init_screenshot_info{ name="main_liaotian_info", zh_name = "聊天处理", info = main_liaotian_info};
    full_str = full_str + "init_screenshot_info{ name=" 
    full_str = full_str + "\"" + input_dict["name_en"] + "_info\",  "
    full_str = full_str + "zh_name = "
    full_str = full_str + "\"" + input_dict["name_cn"] + "\",  "
    full_str = full_str + "info = " +input_dict["name_en"] + "_info"
    full_str = full_str + "};\n\n"

    return full_str


def analysis_row_data(input_dict):
    print(input_dict["name_en"]);
    if input_dict["info"] == "" :
        return do_point_info(input_dict);
    else:
        return do_shot_info(input_dict);


def kobe_trans_excel_file_2_lua_table(file):
    list = excel_table_by_index(file, );
    print(len(list));
    with codecs.open(my_out_file,"w","utf-8") as f:
        f.write("\n");
        for x in xrange(0,len(list)):
            my_str = analysis_row_data(list[x]);
            if "" != my_str :
                f.write(my_str);
        f.close();

print my_file;
kobe_trans_excel_file_2_lua_table(my_file);