
#http://blog.csdn.net/lainegates/article/details/8314287  #pyqt下QTableWidget使用方法小结


在使用pyqt 中QTableWidget设计表格窗口时，通过如下设置可以指定某个行或者列的大小：
self.MyTable.setColumnWidth(2,50)  #将第2列的单元格，设置成50宽度
self.MyTable.setRowHeight(2,60)      #将第2行的单元格，设置成60的高度
现在的问题是对于自动生成的表格带列表头即行号时，有什么方法可以固定行数字所对应的宽度，比如
self.MyTable.setColumnWidth(0,20)  #将设置第1列的单元格成20宽度
self.MyTable.setColumnWidth(1,30)  #将设置第2列的单元格成30宽度
self.MyTable.setColumnWidth(2,50)  #将设置第3列的单元格成50宽度 