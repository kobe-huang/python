# -*- coding: utf-8 -*-

"""
Module implementing LaserMainWindow.
"""
from PyQt5  import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog  

from PyQt5.QtGui import QIntValidator
from ui.Ui_main_window import Ui_LaserMainWindow
# import const_data.my_data
# # const_data.my_data.funA();
# #from const_data.my_data import funA
# const_data.my_data.funA();
# 

class laser_data()
    def __init__(self, parent=None):
        


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
        self.orig_data = None;
        self.debug     = True;
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
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
        item.setText('1');
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.tableWidget_print_list.setItem(0, 0, item)
        #设置只能设置为数字
        self.textEdit_begin_num.setValidator(QIntValidator(1, 65535, self))
        self.textEdit_end_num.setValidator(QIntValidator(1, 65535, self))
    
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_filter_num_clicked(self):
        tmp_begin = int(self.textEdit_begin_num.text())
        tmp_end   = int(self.textEdit_end_num.text())
        print("索引： " + str(tmp_begin) + " "+ str(tmp_end))

        self.tableWidget_print_list.clearContents();
        self.tableWidget_print_list.setRowCount(int(tmp_end) - int(tmp_begin))
        tmp_name = self.comboBox_select_items.currentText(); 
        for i in range(int(tmp_begin), int(tmp_end) ):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
            item.setText(str(i -int(tmp_begin) +1));
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget_print_list.setItem(i-int(tmp_begin), 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i));
            self.tableWidget_print_list.setItem(i-int(tmp_begin), 1, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(self.orig_data[tmp_name][i]);
            self.tableWidget_print_list.setItem(i-int(tmp_begin), 3, item)
            

             
    @pyqtSlot()
    def on_pushButton_mix_table_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_create_table_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
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
        # TODO: not implemented yet
        raise NotImplementedError
    
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
    def on_comboBox_select_items_objectNameChanged(self, objectName):
        """
        Slot documentation goes here.
        
        @param objectName DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_comboBox_select_items_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        tmp_name = self.comboBox_select_items.currentText();
        self.tableWidget_print_list.setRowCount(len(self.orig_data[tmp_name]))
        for i in range(len(self.orig_data[tmp_name])):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
            item.setText(str(i+1));
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget_print_list.setItem(i, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(self.orig_data[tmp_name][i]);
            self.tableWidget_print_list.setItem(i, 3, item)
        self.tableWidget_print_list.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_print_list.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配 
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


    
    @pyqtSlot()
    def on_pushButton_deal_excel_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # pass;
        file_name = self.textEdit_product_file.text();
        # import os.path
        # tmp_file_name = os.path.basename(file_name)
        tmp_file_name = file_name.split("/")[-1]
        self.label_custom_file.setText(tmp_file_name);
        print(file_name)
        from action.excel.do_customer_info import excel_table_by_index_2
        self.orig_data = excel_table_by_index_2(file_name);
        print("---------------");
        self.comboBox_select_items.objectNameChanged.disconnect(self.on_comboBox_select_items_objectNameChanged)
        self.comboBox_select_items.currentIndexChanged['QString'].disconnect(self.on_comboBox_select_items_currentIndexChanged)
        self.comboBox_select_items.clear();
        tmp_num = 0
        for k in self.orig_data.keys():
            self.comboBox_select_items.insertItem(tmp_num,k);
            tmp_num = tmp_num + 1;
            print(k);
        print("+++++++++++++++");
        for v in self.orig_data.values():
            print(v[0]);
        self.comboBox_select_items.currentIndexChanged['QString'].connect(self.on_comboBox_select_items_currentIndexChanged)    
        tmp_name = self.comboBox_select_items.currentText();
        self.tableWidget_print_list.setRowCount(len(self.orig_data[tmp_name]))
        for i in range(len(self.orig_data[tmp_name])):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)         #QtCore.Qt.Unchecked 未选 ，QtCore.Qt.Unchecked 已选
            item.setText(str(i+1));
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget_print_list.setItem(i, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(self.orig_data[tmp_name][i]);
            self.tableWidget_print_list.setItem(i, 3, item)
        self.tableWidget_print_list.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.tableWidget_print_list.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
            

        #self.comboBox_select_items.setCurrentIndex(1);
        # self.comboBox_select_items.currentIndexChanged['QString'].connect(LaserMainWindow.close)
        # self.comboBox_select_items.currentIndexChanged['int'].connect(LaserMainWindow.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = LaserMainWindow()
    ui.adjust_widget_info();
    ui.show()
    sys.exit(app.exec_())