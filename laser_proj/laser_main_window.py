# -*- coding: utf-8 -*-

"""
Module implementing LaserMainWindow.
"""
from PyQt5  import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import pyqtSlot, QDateTime
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog  
from PyQt5.QtWidgets import QMessageBox  

from PyQt5.QtGui import QIntValidator
from ui.Ui_main_window import Ui_LaserMainWindow

import os.path
from laser_main import laser_main
from lib.lib_log import log_info
import time

class LaserMainWindow(  QMainWindow, Ui_LaserMainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        log_info.output("ui_main_init")
        self.main = laser_main();     #获取核心
        self.operator_id    = 999999;
        self.custom_id      = 999999;
        self.type_id        = 999999;
        self.print_num      = 0;
        self.current_index  = 0;
        self.print_list     = {};

        super(LaserMainWindow, self).__init__(parent)
        self.setupUi(self)

    def adjust_widget_info(self):
        #表格
        #self.tableWidget_print_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #PyQt5.QtWidgets.QAbstractItemView
        self.tableWidget_print_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_print_list.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_print_list.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
        self.tableWidget_print_list.verticalHeader().setVisible(False)
        # self.MyTable.verticalHeader().setVisible(False)
        # self.MyTable.horizontalHeader().setVisible(False)
        self.tableWidget_combo_select.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_combo_select.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_combo_select.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
        self.tableWidget_combo_select.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
        item.setText('1');
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.tableWidget_print_list.setItem(0, 0, item)
        #设置只能设置为数字
        self.textEdit_begin_num.setValidator(QIntValidator(1, 65535, self))
        self.textEdit_end_num.setValidator(QIntValidator(1, 65535, self))
    
    def set_last_info(self):
        # self.config_data["user_file_path"]      = self.root_path; #输出的位置
        # self.config_data["user_excel_file"]     = None; #"sl_null";      #上次的文件地址 
        # self.config_data["user_select_index"]   = None# "sl_null";      #上次的index
        # self.config_data["user_operator_name"]  = None#"sl_null";      #商城的操作员名字
        # self.config_data["user_begin_index"]    = None#sl_null";      #上次的起始index
        # self.config_data["user_end_index"]      = None#"sl_null";      #上次的结束index

        #设置操作员
        user_operator_name = self.main.get_config("user_operator_name")
        operator_list = self.main.get_all_operator_name();
        self.comboBox_select_operator.clear()
        self.comboBox_select_operator.insertItem(0, "新操作员");
        if False != operator_list:  
            for i in range(len(operator_list)):
                self.comboBox_select_operator.insertItem(i+1, operator_list[i]);
                self.comboBox_select_operator.setCurrentIndex(0);

        if user_operator_name is not None:
            self.textEdit_operator_name.setText(user_operator_name)
            if user_operator_name in operator_list: #如果在列表中
                self.comboBox_select_operator.setCurrentText(user_operator_name);
        else:
            self.textEdit_operator_name.setText("默认操作员")


        #设置客户
        user_custom_name = self.main.get_config("user_custom_name")
        custom_list = self.main.get_all_custom_name();
        self.comboBox_select_custom.clear()
        self.comboBox_select_custom.insertItem(0, "新客户");
        if False != custom_list:  
            for i in range(len(custom_list)):
                self.comboBox_select_custom.insertItem(i+1, custom_list[i]);
                self.comboBox_select_custom.setCurrentIndex(0);  

        if user_custom_name is not None:
            self.textEdit_custom_name.setText(user_custom_name)
            if user_custom_name in custom_list:  #如果在列表中
                self.comboBox_select_custom.setCurrentText(user_custom_name);
        else:
            self.textEdit_custom_name.setText("默认用户")

        #设置保存路径
        print_output_path = self.main.get_config("print_output_path")
        if print_output_path is not None:
            self.textEdit_output_path.setText(print_output_path)

        #设置用户文件
        user_excel_file = self.main.get_config("user_excel_file")
        if user_excel_file is not None:
            self.textEdit_product_file.setText(user_excel_file)
            self.label_custom_file.setText("客户文件信息:"+ user_excel_file)
        else:
            self.textEdit_product_file.setText("请输入用户表格")
            self.label_custom_file.setText( "客户文件信息: 无") 

        #设置开始
        user_begin_index = self.main.get_config("user_begin_index")
        if user_begin_index is not None:
            self.textEdit_begin_num.setText(str(user_begin_index))
        else:
            self.textEdit_begin_num.setText("1")

        #设置结束
        user_end_index = self.main.get_config("user_end_index")
        if user_end_index is not None:
            self.textEdit_end_num.setText(str(user_end_index))
        else:
            self.textEdit_end_num.setText("1")

    @pyqtSlot(str)
    def on_comboBox_select_operator_currentIndexChanged(self, p0, isInit = False):
        tmp_name = self.comboBox_select_operator.currentText();
        self.textEdit_operator_name.setText(tmp_name)
    @pyqtSlot(str)
    def on_comboBox_select_custom_currentIndexChanged(self, p0, isInit = False):
        tmp_name = self.comboBox_select_custom.currentText();
        self.textEdit_custom_name.setText(tmp_name)




    def do_last_info(self):
        #检查用户表格，并读入
        file_name = self.textEdit_product_file.text();
        if False == os.path.exists(file_name):
            return
        else:
            self.on_pushButton_deal_excel_clicked(True);
        pass
        #筛选
        #self.on_pushButton_filter_num_clicked();
    def enable_all_widget(self,flag = True):
        self.tableWidget_print_list.setEnabled(flag)
        self.pushButton_edit_item.setEnabled(flag)
        self.pushButton_create_table.setEnabled(flag)
        self.pushButton_exit.setEnabled(flag)

        self.checkBox_select_all.setEnabled(flag)
        self.checkBox_select_unprint.setEnabled(flag)
        self.checkBox_select_invert.setEnabled(flag)
        self.comboBox_select_items.setEnabled(flag)
        self.pushButton_select_excel_file.setEnabled(flag)
        self.pushButton_deal_excel.setEnabled(flag)

        self.textEdit_product_file.setEnabled(flag)
        self.label_custom_file.setEnabled(flag)
        self.textEdit_begin_num.setEnabled(flag)
        self.textEdit_end_num.setEnabled(flag)
        self.pushButton_filter_num.setEnabled(flag)
        self.label_total_num.setEnabled(flag)

        self.progressBar_print.setEnabled(flag)
        self.pushButton_stop.setEnabled(flag)

        self.textEdit_operator_name.setEnabled(flag)
        self.textEdit_custom_name.setEnabled(flag)
        self.pushButton_start.setEnabled(flag)

        self.textEdit_custom_name.setEnabled(flag)
        self.textEdit_operator_name.setEnabled(flag)
        self.comboBox_select_custom.setEnabled(flag)
        self.comboBox_select_operator.setEnabled(flag)

        self.checkBox_group_print.setEnabled(flag)
        self.tableWidget_combo_select.setEnabled(flag)

        self.pushButton_select_output_path.setEnabled(flag)
        self.textEdit_output_path.setEnabled(flag)


    def set_progress_bar(self, total = 10, now_index = 5):
        self.progressBar_print.setMaximum(total)
        self.progressBar_print.setValue(now_index)
        self.progressBar_print.setFormat( "进度: " + str(now_index) + "/" + str(total));

    def start_print(self):
        output_path = self.textEdit_output_path.text();        
        #删除文件夹下的文件
        exts  = ".kobe.txt"
        files = os.listdir(output_path)
        for name in files:
            if(name.endswith(exts)):
                os.remove(os.path.join(output_path, name))
        #开始写文件
        for k in self.print_list.keys():
            file_name = os.path.join(output_path, "__"+k+exts)
            file_hdl = open(file_name, 'w')
            for print_item in self.print_list[k]:  
                print(print_item);
                file_hdl.write(print_item + "\n")       
            file_hdl.close();



        self.enable_all_widget(False) #启动这个
        self.pushButton_stop.setEnabled(True) #启动这个
        self.progressBar_print.setEnabled(True)
        self.textEdit_stop_index.setEnabled(True)

        self.hand_deal_with()
        
        # self.enable_all_widget(True) #启动这个
        # self.pushButton_stop.setEnabled(False) #启动这个
        # self.textEdit_stop_index.setEnabled(False)
        # self.on_pushButton_filter_num_clicked();


        #onpushButton_filter_num   
        #self.main.insert_print_info(self.operator_id, self.type_id, self.custom_id, print_item)        
        #self.on_pushButton_filter_num_clicked();
    def hand_deal_with(self): #手动处理
        self.textEdit_stop_index.setText(str(self.print_num));
        print("hand_deal_with")



    def test_xxxxx(self,print_list):
        print("test_xxxxx")
        for i in range(len(print_list)):  
            print(self.operator_id);
            print(self.type_id);
            print(self.custom_id);
            print(print_list[i]);

            self.main.insert_print_info(self.operator_id, self.type_id, self.custom_id, print_list[i])
            self.set_progress_bar(len(print_list), i+1)
            time.sleep(0.1);



    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        self.enable_all_widget(True)

        self.pushButton_stop.setEnabled(False) 
        stop_index = int(self.textEdit_stop_index.text())
        self.textEdit_stop_index.setEnabled(False) 
        
        if self.checkBox_group_print.checkState() == QtCore.Qt.Checked:
           self.tableWidget_combo_select.setEnabled(True) 
        else: 
            self.tableWidget_combo_select.setEnabled(False)
        for i in range(stop_index):
            for k in self.print_list.keys():
                type_id = int(self.main.insert_print_type(k) )
                self.main.insert_print_info(self.operator_id, type_id, self.custom_id, self.print_list[k][i])
        self.on_pushButton_filter_num_clicked();
    
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        tmp_type_name   = self.comboBox_select_items.currentText();
        self.type_id    = self.main.insert_print_type(tmp_type_name)
        self.print_list = {};
        #检查设置的信息
        tmp_custom_name = self.textEdit_custom_name.text()
        if tmp_custom_name == "":
            QMessageBox.information( self, "警告", "请设置客户" )
            return; 
        else:
            self.custom_id = self.main.insert_custom(tmp_custom_name)
            self.main.set_config("user_custom_name", tmp_custom_name);


        tmp_operator_name =self.textEdit_operator_name.text();
        if tmp_operator_name == "":
            QMessageBox.information( self, "警告", "请设置操作员" )
            return;
        else:
            self.operator_id = self.main.insert_operator(tmp_operator_name)
            self.main.set_config("user_operator_name", tmp_operator_name);

        
        if False == os.path.exists(self.textEdit_output_path.text()):
            QMessageBox.information( self, "警告", "请设置导出路径" )
            return;


        ############################################################
        print_num = 0;
        had_print = 0;
         

        tmp_str = " "
        print_type_list = {};
        print_type_list[self.comboBox_select_items.currentText()] = []  #设置成空列表
        if self.checkBox_group_print.checkState() == QtCore.Qt.Checked:
            tmp_row_count_1 = self.tableWidget_combo_select.rowCount()
            for i in range(tmp_row_count_1):
                if self.tableWidget_combo_select.item(i, 0).checkState() == QtCore.Qt.Checked:
                    #tmp_str = tmp_str + " " + self.tableWidget_combo_select.item(i, 1).text();
                    print_type_list[self.tableWidget_combo_select.item(i, 1).text()] = []#设置成空列表

        for k in print_type_list.keys():
            tmp_str = " &" + k + tmp_str      
        tmp_str  = " 组：" + tmp_str;
        
        
        tmp_row_count = self.tableWidget_print_list.rowCount()
        for i in range(tmp_row_count):
            if self.tableWidget_print_list.item(i, 0).checkState() == QtCore.Qt.Checked :
                #tmp_print_list.append(self.tableWidget_print_list.item(i, 3).text())
                tmp_index = int(self.tableWidget_print_list.item(i, 1).text())
                for k in print_type_list.keys():
                    print_type_list[k].append(self.main.orig_data[k][tmp_index-1])

                if "已经打印" == self.tableWidget_print_list.item(i, 2).text():
                    had_print = had_print + 1;
                print_num = print_num + 1;

        

        if print_num == 0:
             QMessageBox.information( self, "警告", "未选中任何打印")
             return;

        self.print_list = print_type_list; #设置打印列表

        self.print_num = print_num;  
        msg_info = "打印数量："+str(print_num) + " 已打印："+str(had_print);
        msg_info = msg_info + tmp_str;
        R = QMessageBox.question( self, "确认", msg_info , QMessageBox.Yes, QMessageBox.No)## 弹出询问框  
        if R == QMessageBox.Yes:
            print("开始工作");           
            self.start_print();
        else:
            print("取消")


    
    @pyqtSlot()
    def on_pushButton_filter_num_clicked(self):
        tmp_begin = int(self.textEdit_begin_num.text())
        tmp_end   = int(self.textEdit_end_num.text())
        print("索引： " + str(tmp_begin) + " "+ str(tmp_end))
        tmp_name = self.comboBox_select_items.currentText();

        #self.tableWidget_print_list.setRowCount(len(self.main.orig_data[tmp_name]))
        if (tmp_begin > tmp_end) or (tmp_end > len(self.main.orig_data[tmp_name]) ):
            QMessageBox.information( self, "警告", "设置错误" )
            return;

        self.tableWidget_print_list.clearContents();
        self.tableWidget_print_list.setRowCount(int(tmp_end) - int(tmp_begin) + 1)
        tmp_name = self.comboBox_select_items.currentText(); 
        for i in range(int(tmp_begin), int(tmp_end)+1 ):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
            item.setText(str(i -int(tmp_begin) +1 ));
            self.tableWidget_print_list.setItem(i-int(tmp_begin), 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i));
            self.tableWidget_print_list.setItem(i -int(tmp_begin), 1, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(self.main.orig_data[tmp_name][i-1]);
            self.tableWidget_print_list.setItem(i -int(tmp_begin), 3, item)

            item = QtWidgets.QTableWidgetItem()
            if True == self.main.check_print_info(self.main.orig_data[tmp_name][i-1]):
                item.setText("已经打印");
            else:
                item.setText("未打印");
            self.tableWidget_print_list.setItem(i-int(tmp_begin), 2, item)


            self.main.set_config("user_begin_index", tmp_begin)
            self.main.set_config("user_end_index", tmp_end)

        self.tableWidget_print_list.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_print_list.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
 

    @pyqtSlot()
    def on_pushButton_mix_table_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.information( self, "警告", "未完成")

    @pyqtSlot()
    def on_pushButton_select_output_path_clicked(self):
        """
        Slot documentation goes here.
        """
        selectDirName = QFileDialog.getExistingDirectory(None,"选择文件夹","D:\\")## 弹出对话框，选择文件夹 
        if selectDirName is not None:
            self.textEdit_output_path.setText(selectDirName)
            print("+++++++++"+selectDirName);
            self.main.set_config("print_output_path", selectDirName);

    
    @pyqtSlot()
    def on_pushButton_create_table_clicked(self):
        """
        Slot documentation goes here.
        """
        # fileName1, filetype = QFileDialog.getSaveFileName(self,  
        #                             "选取文件",  
        #                             "C:\\Users\\abc-pc\\Desktop",  
        #                             "excel Files (*.xls);;excel Files (*.xlsx)")  #设置文件扩展名过滤,注意用双分号间隔  
        # print(fileName1,filetype)
        # print_info = self.main.get_print_info()
        # if False == print_info:
        #     QMessageBox( self, "警告", "没有数据" )
        # else:
        #     from action.excel.do_customer_info import write_excel
        #     write_excel(fileName1, print_info)
        from ui.save_table_dialog import saveTableDialog
        from ui.save_table_dialog import saveTableDialog
        #show_dialog()
        self.my_dialog = saveTableDialog();
        self.my_dialog.main = self.main;
        self.my_dialog.fill_combo_list();
        self.my_dialog.show();

        # import time
        # time.sleep(10)
        
    @pyqtSlot(str)
    def on_comboBox_start_index_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_comboBox_end_index_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(int)
    def on_checkBox_select_all_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """

        tmp_row_count = self.tableWidget_print_list.rowCount() 
        # pass;
        # tmp_row_count = 10
        print("-------" + str(tmp_row_count));
        print("++++++" + str(p0));
        if 0 == p0:
            for i in range(tmp_row_count):
                self.tableWidget_print_list.item(i, 0).setCheckState(QtCore.Qt.Unchecked);
        else:
            for i in range(tmp_row_count):
                self.tableWidget_print_list.item(i, 0).setCheckState(QtCore.Qt.Checked);

    
    @pyqtSlot(int)
    def on_checkBox_select_unprint_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        tmp_row_count = self.tableWidget_print_list.rowCount() 
        # pass;
        # tmp_row_count = 10
        for i in range(tmp_row_count):
            if "未打印" == self.tableWidget_print_list.item(i, 2).text():
                self.tableWidget_print_list.item(i, 0).setCheckState(QtCore.Qt.Checked);
            else:
                self.tableWidget_print_list.item(i, 0).setCheckState(QtCore.Qt.Unchecked);
        
            
    @pyqtSlot(int)
    def on_checkBox_select_invert_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        #raise NotImplementedError

        tmp_row_count = self.tableWidget_print_list.rowCount() 
        # pass;
        # tmp_row_count = 10
        for i in range(tmp_row_count):
            if self.tableWidget_print_list.item(i, 0).checkState() == QtCore.Qt.Unchecked :
                self.tableWidget_print_list.item(i, 0).setCheckState(QtCore.Qt.Checked);
            else:
                self.tableWidget_print_list.item(i, 0).setCheckState(QtCore.Qt.Unchecked);

    @pyqtSlot(str)
    def on_comboBox_select_items_currentIndexChanged(self, p0, isInit = False):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        tmp_name = self.comboBox_select_items.currentText();
        print("shezhi+++: " + str(len(self.main.orig_data[tmp_name])));
        # self.tableWidget_print_list.setRowCount(len(self.main.orig_data[tmp_name]))
        
        # for i in range(len(self.main.orig_data[tmp_name])):
        #     item = QtWidgets.QTableWidgetItem()
        #     item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
        #     item.setText(str(i+1));
        #     item.setTextAlignment(QtCore.Qt.AlignHCenter)
        #     self.tableWidget_print_list.setItem(i, 0, item)

        #     item = QtWidgets.QTableWidgetItem()
        #     item.setText(self.main.orig_data[tmp_name][i]);
        #     self.tableWidget_print_list.setItem(i, 3, item)

        # self.tableWidget_print_list.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        # self.tableWidget_print_list.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
        if True == isInit:
            self.textEdit_begin_num.setText(str(self.main.get_config("user_begin_index"))); 
            self.textEdit_end_num.setText(str(self.main.get_config("user_end_index"))); 
        else:
            self.textEdit_begin_num.setText(str(1)); 
            self.textEdit_end_num.setText(str(len(self.main.orig_data[tmp_name]))); 

        self.on_pushButton_filter_num_clicked();
        self.label_total_num.setText("总条目："+str(len(self.main.orig_data[tmp_name])))
        self.main.set_config("user_select_index", self.comboBox_select_items.currentIndex())   #设置配置文件
    
    @pyqtSlot()
    def on_pushButton_select_excel_file_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        fileName1, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:\\Users\\abc-pc\\Desktop",  
                                    "excel Files (*.xlsx);;excel Files (*.xls)")  #设置文件扩展名过滤,注意用双分号间隔  
        print(fileName1,filetype)  
        self.textEdit_product_file.setText(fileName1);


    def init_combo_print_table(self):
        # for k in self.main.orig_data.keys():
        #     self.comboBox_select_items.insertItem(tmp_num,k);
        #     tmp_num = tmp_num + 1;
        #     print(k);
        self.tableWidget_combo_select.clearContents();
        self.tableWidget_combo_select.setRowCount(len(self.main.orig_data))
        tmp_num = 0
        for k in self.main.orig_data.keys():
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)   #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
            #item.setText(str(tmp_num+1)+"."+k);
            item.setText(str(tmp_num+1));
            self.tableWidget_combo_select.setItem(tmp_num, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(k);
            self.tableWidget_combo_select.setItem(tmp_num, 1, item)

            tmp_num = tmp_num +1
        self.tableWidget_combo_select.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_combo_select.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配

    @pyqtSlot(int)
    def on_checkBox_group_print_stateChanged(self, p0):
        if 0 == p0:
            self.tableWidget_combo_select.setEnabled(False)
        else:
            self.tableWidget_combo_select.setEnabled(True)


    @pyqtSlot()
    def on_pushButton_deal_excel_clicked(self, isInit = False):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # pass;
        file_name = self.textEdit_product_file.text();
        if False == os.path.exists(file_name):
            QMessageBox.information( self, "警告", "文件路径异常" )
            return;


        tmp_file_name = file_name.split("/")[-1]
        self.label_custom_file.setText(tmp_file_name);
        print(file_name)
        from action.excel.do_customer_info import excel_table_by_index_2
        self.main.orig_data = excel_table_by_index_2(file_name);
        print("---------------");
        self.comboBox_select_items.currentIndexChanged['QString'].disconnect(self.on_comboBox_select_items_currentIndexChanged)
        self.comboBox_select_items.clear();
        tmp_num = 0 #设置下拉选择
        for k in self.main.orig_data.keys():
            self.comboBox_select_items.insertItem(tmp_num,k);
            tmp_num = tmp_num + 1;
            print(k); 

        self.init_combo_print_table();       

        print("+++++++++++++++");
        for v in self.main.orig_data.values():
            print(v[0]);
        #self.comboBox_select_items.currentIndexChanged['QString'].connect(self.on_comboBox_select_items_currentIndexChanged)         
        tmp_select_index = 0;
        if True == isInit:
            #self.comboBox_select_items.setCurrentIndex(int(self.main.get_config("user_select_index")))
            tmp_select_index = int(self.main.get_config("user_select_index"));
            print("设置上次+++")
            #return;
        self.comboBox_select_items.setCurrentIndex(tmp_select_index);
        if True == isInit:
            self.on_comboBox_select_items_currentIndexChanged("0", True);
        else:
            self.on_comboBox_select_items_currentIndexChanged("0");

        self.comboBox_select_items.currentIndexChanged['QString'].connect(self.on_comboBox_select_items_currentIndexChanged)

        self.tableWidget_print_list.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_print_list.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
         
        #设置配置文件    
        self.main.set_config("user_excel_file",   file_name)
        self.main.set_config("user_select_index", self.comboBox_select_items.currentIndex() )


if __name__ == "__main__":
    import sys
    log_info.file_path =  os.path.split(os.path.realpath(__file__))[0]+"\\log.txt" 
    app = QtWidgets.QApplication(sys.argv)
    ui = LaserMainWindow()
    ui.adjust_widget_info();
    ui.set_last_info()
    ui.do_last_info()

    ui.show()
    sys.exit(app.exec_())