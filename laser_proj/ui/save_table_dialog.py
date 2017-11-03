# -*- coding: utf-8 -*-

"""
Module implementing saveTableDialog.
"""

from PyQt5.QtCore import pyqtSlot, QDateTime
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog  
from PyQt5.QtWidgets import QMessageBox  

from .Ui_save_table_dialog import Ui_saveTableDialog
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
sys.path.append("..")
from laser_main import laser_main
import time
import os

class saveTableDialog(QDialog, Ui_saveTableDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, ):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(saveTableDialog, self).__init__(parent)
        self.setupUi(self)
        self.main = None
        # self.fill_combo_list()
    
    def fill_combo_list(self):
        self.comboBox_operator.clear()
        self.comboBox_operator.insertItem(0, "全部");
        if self.checkBox_filter.checkState() == QtCore.Qt.Checked:
            tmp_str = self.lineEdit_operator.text()
            if tmp_str == "":
                fetch_all = self.main.get_all_operator_name();
            else:
                print(tmp_str);
                fetch_all = self.main.get_part_operator_name(tmp_str); 
        else:
            fetch_all = self.main.get_all_operator_name();
        print(fetch_all)
        for i in range(len(fetch_all)):
            self.comboBox_operator.insertItem(i+1, fetch_all[i]);
        self.comboBox_operator.setCurrentIndex(0);



        self.comboBox_custom.clear()
        self.comboBox_custom.insertItem(0, "全部");
        if self.checkBox_filter.checkState() == QtCore.Qt.Checked:
            tmp_str = self.lineEdit_custom.text()
            if tmp_str == "":
                fetch_all = self.main.get_all_custom_name();
            else:
                fetch_all = self.main.get_part_custom_name(tmp_str); 
        else:
            fetch_all = self.main.get_all_custom_name();
        for i in range(len(fetch_all)):
            self.comboBox_custom.insertItem(i+1, fetch_all[i]);
        self.comboBox_custom.setCurrentIndex(0);

        self.comboBox_type.clear()
        self.comboBox_type.insertItem(0, "全部");
        fetch_all = self.main.get_all_type_name();
        for i in range(len(fetch_all)):
            self.comboBox_type.insertItem(i+1, fetch_all[i]);
        self.comboBox_type.setCurrentIndex(0);


    @pyqtSlot(int)
    def on_checkBox_filter_stateChanged(self, p0):
        if 0 == p0:
            self.lineEdit_operator.setEnabled(True)
            self.lineEdit_custom.setEnabled(True)
            self.fill_combo_list()
        else:
            self.lineEdit_operator.setEnabled(False)
            self.lineEdit_custom.setEnabled(False)
            self.fill_combo_list()



    @pyqtSlot()
    def on_calendarWidget_end_selectionChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        date_begin = self.calendarWidget_begin.selectedDate()
        date_end = self.calendarWidget_end.selectedDate()
        data_str = date_begin.toString("yyyy-MM-dd") + " --> " + date_end.toString("yyyy-MM-dd")
        self.label_data_txt.setText("日期： "+data_str)
    
    @pyqtSlot()
    def on_calendarWidget_begin_selectionChanged(self):
        self.on_calendarWidget_end_selectionChanged()
        
    
    @pyqtSlot(int)
    def on_checkBox_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        if 0 == p0:
            self.calendarWidget_begin.setEnabled(False)
            self.calendarWidget_end.setEnabled(False)
            self.label_data_txt.setText("当天数据")
        else:
            self.calendarWidget_begin.setEnabled(True)
            self.calendarWidget_end.setEnabled(True)
    
    def check_print_setting(self):
        search_str = "";
        tmp_num = 0;
        datetime = QDateTime();


        if self.checkBox.checkState() == QtCore.Qt.Checked:
            date_begin  = self.calendarWidget_begin.selectedDate()
            date_end    = self.calendarWidget_end.selectedDate()

            # data_begin_str  = date_begin.toString("yyyy-MM-dd") + "  00:00:01:541"
            # data_end_str    = date_end.toString("yyyy-MM-dd") + "  23:59:59:541"
            # start_tick      = datetime.fromString(data_begin_str, "yyyy-MM-dd hh:mm:ss:zzz").toTime_t();
            # end_tick        = datetime.fromString(data_end_str, "yyyy-MM-dd hh:mm:ss:zzz").toTime_t();
            #time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
            data_begin_str  = date_begin.toString("yyyy-MM-dd") + " 00:00:01"
            data_end_str    = date_end.toString("yyyy-MM-dd") + " 23:59:59"
            start_tick = int(time.mktime(time.strptime(data_begin_str,'%Y-%m-%d %H:%M:%S')))
            end_tick   = int(time.mktime(time.strptime(data_end_str,'%Y-%m-%d %H:%M:%S')))

            if start_tick > end_tick:
                QMessageBox( self, "警告", "时间设置错误" )
                return False

            search_str      = search_str + " where print_time_s > " + str(start_tick) 
            search_str      = search_str + " and print_time_s < " + str(end_tick) 

        else:
            today_str = datetime.currentDateTime().toString("yyyy-MM-dd");
            # today_str = today_str + "  00:00:01:541"
            # start_tick = datetime.fromString(today_str, "yyyy-MM-dd hh:mm:ss:zzz").toTime_t();
            
            today_str  = today_str + " 00:00:01"
            start_tick = int(time.mktime(time.strptime(today_str,'%Y-%m-%d %H:%M:%S')))
            search_str = search_str + " where print_time_s > " + str(start_tick)
        
        #-----------------------------
        tmp_str = self.comboBox_operator.currentText()
        if tmp_str == "全部":
            print("全部");
        else:
            tmp_num = self.main.insert_operator(tmp_str)
            search_str = search_str + " and operator_id = " + str(tmp_num)
        #-----------------------------
        tmp_str = self.comboBox_custom.currentText()
        if tmp_str == "全部":
            print("全部");
        else:
            tmp_num = self.main.insert_custom(tmp_str)
            search_str = search_str + " and custom_id = " + str(tmp_num)
        #-----------------------------
        tmp_str = self.comboBox_type.currentText()
        if tmp_str == "全部":
            print("全部");
        else:
            tmp_num = self.main.insert_print_type(tmp_str)
            search_str = search_str + " and type_id = " + str(tmp_num)

        return search_str;
        



    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        sear_str = self.check_print_setting();
        
        if False == sear_str:
            return;
        save_name = "操作员-"+self.comboBox_operator.currentText()+"&"
        save_name = save_name + "客户-"+self.comboBox_custom.currentText()+"&"
        save_name = save_name + "项目-" +self.comboBox_type.currentText()+"&"
        save_name = save_name + QDateTime.currentDateTime().toString("yyyy-MM-dd");
        save_path = self.main.get_config("save_excel_path")
        if save_path is None:
            save_path = "D:\\"

        fileName1, filetype = QFileDialog.getSaveFileName(self,  
                                    "选取文件",  
                                    os.path.join(save_path,save_name),  
                                    "excel Files (*.xls);;excel Files (*.xlsx)")  #设置文件扩展名过滤,注意用双分号间隔  
        print(fileName1,filetype)
        self.main.set_config("save_excel_path",os.path.split(fileName1)[0]);

        print_info = self.main.get_print_info(sear_str)
        if False == print_info:
            QMessageBox( self, "警告", "没有数据" )
        else:
            from action.excel.do_customer_info import write_excel
            write_excel(fileName1, print_info)
        self.close()


               

def show_dialog(main_ds = None):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # saveTableDialog = QtWidgets.QDialog()
    ui = saveTableDialog()
    # ui.setupUi(saveTableDialog)
    ui.show()
    sys.exit(app.exec_())

#show_dialog()