# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\kobe_doc\code\github\python\laser_proj\ui\save_table_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saveTableDialog(object):
    def setupUi(self, saveTableDialog):
        saveTableDialog.setObjectName("saveTableDialog")
        saveTableDialog.resize(488, 368)
        self.calendarWidget_end = QtWidgets.QCalendarWidget(saveTableDialog)
        self.calendarWidget_end.setEnabled(False)
        self.calendarWidget_end.setGeometry(QtCore.QRect(240, 30, 241, 191))
        self.calendarWidget_end.setObjectName("calendarWidget_end")
        self.calendarWidget_begin = QtWidgets.QCalendarWidget(saveTableDialog)
        self.calendarWidget_begin.setEnabled(False)
        self.calendarWidget_begin.setGeometry(QtCore.QRect(0, 30, 241, 191))
        self.calendarWidget_begin.setObjectName("calendarWidget_begin")
        self.comboBox_operator = QtWidgets.QComboBox(saveTableDialog)
        self.comboBox_operator.setGeometry(QtCore.QRect(60, 270, 101, 21))
        self.comboBox_operator.setObjectName("comboBox_operator")
        self.label = QtWidgets.QLabel(saveTableDialog)
        self.label.setGeometry(QtCore.QRect(10, 270, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(saveTableDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 41, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_custom = QtWidgets.QComboBox(saveTableDialog)
        self.comboBox_custom.setGeometry(QtCore.QRect(60, 300, 101, 21))
        self.comboBox_custom.setObjectName("comboBox_custom")
        self.label_3 = QtWidgets.QLabel(saveTableDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 61, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_type = QtWidgets.QComboBox(saveTableDialog)
        self.comboBox_type.setGeometry(QtCore.QRect(60, 330, 101, 21))
        self.comboBox_type.setObjectName("comboBox_type")
        self.checkBox = QtWidgets.QCheckBox(saveTableDialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 230, 71, 28))
        self.checkBox.setObjectName("checkBox")
        self.label_data_txt = QtWidgets.QLabel(saveTableDialog)
        self.label_data_txt.setGeometry(QtCore.QRect(110, 230, 281, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_data_txt.setFont(font)
        self.label_data_txt.setObjectName("label_data_txt")
        self.pushButton_ok = QtWidgets.QPushButton(saveTableDialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(360, 260, 81, 41))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_2 = QtWidgets.QPushButton(saveTableDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 310, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_data_txt_2 = QtWidgets.QLabel(saveTableDialog)
        self.label_data_txt_2.setGeometry(QtCore.QRect(90, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_data_txt_2.setFont(font)
        self.label_data_txt_2.setObjectName("label_data_txt_2")
        self.label_data_txt_3 = QtWidgets.QLabel(saveTableDialog)
        self.label_data_txt_3.setGeometry(QtCore.QRect(340, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_data_txt_3.setFont(font)
        self.label_data_txt_3.setObjectName("label_data_txt_3")
        self.lineEdit_operator = QtWidgets.QLineEdit(saveTableDialog)
        self.lineEdit_operator.setEnabled(True)
        self.lineEdit_operator.setGeometry(QtCore.QRect(190, 270, 101, 21))
        self.lineEdit_operator.setObjectName("lineEdit_operator")
        self.lineEdit_type = QtWidgets.QLineEdit(saveTableDialog)
        self.lineEdit_type.setEnabled(False)
        self.lineEdit_type.setGeometry(QtCore.QRect(190, 330, 101, 21))
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.lineEdit_custom = QtWidgets.QLineEdit(saveTableDialog)
        self.lineEdit_custom.setEnabled(True)
        self.lineEdit_custom.setGeometry(QtCore.QRect(190, 300, 101, 21))
        self.lineEdit_custom.setObjectName("lineEdit_custom")
        self.checkBox_filter = QtWidgets.QCheckBox(saveTableDialog)
        self.checkBox_filter.setGeometry(QtCore.QRect(300, 267, 51, 31))
        self.checkBox_filter.setObjectName("checkBox_filter")

        self.retranslateUi(saveTableDialog)
        self.pushButton_2.clicked.connect(saveTableDialog.close)
        QtCore.QMetaObject.connectSlotsByName(saveTableDialog)

    def retranslateUi(self, saveTableDialog):
        _translate = QtCore.QCoreApplication.translate
        saveTableDialog.setWindowTitle(_translate("saveTableDialog", "Dialog"))
        self.label.setText(_translate("saveTableDialog", "操作员"))
        self.label_2.setText(_translate("saveTableDialog", "客户"))
        self.label_3.setText(_translate("saveTableDialog", "打印项目"))
        self.checkBox.setText(_translate("saveTableDialog", "选择日期"))
        self.label_data_txt.setText(_translate("saveTableDialog", "<html><head/><body><p><span style=\" color:#ff0000;\">自选日期：当天</span></p></body></html>"))
        self.pushButton_ok.setText(_translate("saveTableDialog", "确定"))
        self.pushButton_2.setText(_translate("saveTableDialog", "取消"))
        self.label_data_txt_2.setText(_translate("saveTableDialog", "起始日期"))
        self.label_data_txt_3.setText(_translate("saveTableDialog", "结束日期"))
        self.checkBox_filter.setText(_translate("saveTableDialog", "筛选"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saveTableDialog = QtWidgets.QDialog()
    ui = Ui_saveTableDialog()
    ui.setupUi(saveTableDialog)
    saveTableDialog.show()
    sys.exit(app.exec_())

