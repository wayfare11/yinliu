# Form implementation generated from reading ui file 'c:\Users\WB-wangyu\Desktop\文档\开发文档\DrainageTube\view\viewList.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QCheckBox, QTableWidgetItem, QHeaderView, QPushButton
from dao import viewDao

class ViewList(QWidget):

    def __init__(self, row_id):
        super(ViewList, self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.row_id = row_id
        self.total_pages = 1  # 初始化总页数为1
        self.rows_per_page = 10
        self.now_page = 1
        self.fake_data = None
        self.initTable()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.listName = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.listName.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listName.setFont(font)
        self.listName.setObjectName("listName")
        self.horizontalLayout.addWidget(self.listName)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 80, 1431, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchLineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_2.addWidget(self.searchLineEdit)
        self.searchButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)

        # 绑定搜索按钮点击事件
        self.searchButton.clicked.connect(self.initTable)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.addButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.addButton_3.setObjectName("addButton_3")
        self.horizontalLayout_2.addWidget(self.addButton_3)
        self.deleteButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.deleteButton_2.setObjectName("deleteButton_2")
        self.horizontalLayout_2.addWidget(self.deleteButton_2)

        # 添加删除按钮点击事件
        self.deleteButton_2.clicked.connect(self.batchDeleteButtonClicked)

        self.ViewShowTable = QtWidgets.QTableWidget(parent=Form)
        self.ViewShowTable.setGeometry(QtCore.QRect(30, 140, 1431, 671))
        self.ViewShowTable.setObjectName("ViewShowTable")
        self.ViewShowTable.setColumnCount(0)
        self.ViewShowTable.setRowCount(0)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 820, 1431, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pageSelectBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_3)
        self.pageSelectBox.setObjectName("pageSelectBox")
        self.pageSelectBox.addItem("")
        self.pageSelectBox.addItem("")
        self.pageSelectBox.addItem("")
        self.pageSelectBox.addItem("")
        self.horizontalLayout_3.addWidget(self.pageSelectBox)
        self.pageShowLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.pageShowLabel.setObjectName("pageShowLabel")
        self.horizontalLayout_3.addWidget(self.pageShowLabel)
        self.forwardButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout_3.addWidget(self.forwardButton)

        # 添加前一页按钮点击事件
        self.forwardButton.clicked.connect(self.backwardButtonClicked)

        self.backButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_3.addWidget(self.backButton)

        # 添加后一页按钮点击事件
        self.backButton.clicked.connect(self.forwardButtonClicked)

        self.pageLineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        self.pageLineEdit.setInputMask("")
        self.pageLineEdit.setObjectName("pageLineEdit")
        self.horizontalLayout_3.addWidget(self.pageLineEdit)
        self.goToButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.goToButton.setObjectName("goToButton")
        self.horizontalLayout_3.addWidget(self.goToButton)

        # 新增前往按钮点击事件
        self.goToButton.clicked.connect(self.goToButtonClicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ViewList"))
        self.label.setText(_translate("Form", "清单名称："))
        self.searchLineEdit.setPlaceholderText(_translate("Form", "请输入要查询的名称"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.addButton_3.setText(_translate("Form", "新增"))
        self.deleteButton_2.setText(_translate("Form", "批量删除"))
        self.pageSelectBox.setItemText(0, _translate("Form", "每页10条"))
        self.pageSelectBox.setItemText(1, _translate("Form", "每页20条"))
        self.pageSelectBox.setItemText(2, _translate("Form", "每页50条"))
        self.pageSelectBox.setItemText(3, _translate("Form", "每页100条"))
        self.pageShowLabel.setText(_translate("Form", "第1页/共4页"))
        self.forwardButton.setText(_translate("Form", "前一页"))
        self.backButton.setText(_translate("Form", "后一页"))
        self.pageLineEdit.setPlaceholderText(_translate("Form", "请输入页数"))
        self.goToButton.setText(_translate("Form", "前往"))

        self.pageSelectBox.currentIndexChanged.connect(self.pageComboBoxChanged)

    def batchDeleteButtonClicked(self):
        selected_rows = []  # 存储选中的行的数据
        max_row = min(self.rows_per_page, len(self.fake_data) - (self.now_page - 1) * self.rows_per_page)  # 获取当前页的实际数据量
        for row in range(1, max_row + 1):  # 从第二行开始遍历表格的每一行
            checkbox = self.ViewShowTable.cellWidget(row, 0)  # 获取复选框
            if checkbox and checkbox.isChecked():  # 如果复选框存在且被选中
                # 获取选中行的 id
                selected_id = self.fake_data[(self.now_page - 1) * self.rows_per_page + row - 1][0]
                selected_rows.append(selected_id)  # 将选中行的 id 添加到列表中

        if len(selected_rows) == 0:
             QMessageBox.warning(None, '系统提示', '请选中您需要删除的那行记录！')
             return
        
        reply = QMessageBox.question(self, '系统提示', '您确定要删除这条记录吗？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if viewDao.delete(selected_rows) > 0:
                QMessageBox.information(None, '系统提示', '删除成功')
                self.initTable()
            else:
                QMessageBox.warning(None, '系统提示', '删除失败')

    # 新增下拉框选择显示数据量
    def pageComboBoxChanged(self, index):
        """
        Handle the change in the pageComboBox
        :param index: Index of the selected item in the pageComboBox
        """
        rows_per_page_options = [10, 20, 50, 100]  # Define the available rows per page options
        self.rows_per_page = rows_per_page_options[index]  # Get the selected rows per page value

        # Reinitialize the table based on the selected rows per page
        self.now_page = 1
        self.pageLineEdit.setText("")
        self.initTable()

    def backwardButtonClicked(self):
        if self.now_page > 1:  # 如果当前页不是第一页
            self.now_page -= 1  # 更新当前页数为上一页
            self.pageShowLabel.setText(f"第{self.now_page}页/共{self.total_pages}页")  # 更新页面标签显示
            start_row = (self.now_page - 1) * self.rows_per_page  # 计算起始行
            end_row = self.now_page * self.rows_per_page  # 计算结束行
            self.clearTableExceptHeader()  # 清空表格数据
            self.showPage(start_row, end_row)  # 显示上一页的数据
        # 如果当前页已经是第一页，则点击按钮时不执行任何操作
            
    def forwardButtonClicked(self):
        if self.now_page < self.total_pages:  # 如果当前页不是最后一页
            self.now_page += 1  # 更新当前页数为下一页
            self.pageShowLabel.setText(f"第{self.now_page}页/共{self.total_pages}页")  # 更新页面标签显示
            start_row = (self.now_page - 1) * self.rows_per_page  # 计算起始行
            end_row = min(self.now_page * self.rows_per_page, len(self.fake_data))  # 计算结束行
            self.clearTableExceptHeader()  # 清空表格数据
            self.showPage(start_row, end_row)  # 显示下一页的数据
        # 如果当前页已经是最后一页，则点击按钮时不执行任何操作
            
    def goToButtonClicked(self):
        # Get the input page number
        page_text = self.pageLineEdit.text()
        if page_text.isdigit():  # Check if the input is a number
            page_number = int(page_text)

            if 1 <= page_number <= self.total_pages:
                # Calculate the start and end rows for the specified page
                start_row = (page_number - 1) * self.rows_per_page
                end_row = min(page_number * self.rows_per_page, len(self.fake_data))

                self.now_page = page_number
                self.pageShowLabel.setText(f"第{self.now_page}页/共{self.total_pages}页")

                # Clear the table except for the header row before displaying the new data
                self.clearTableExceptHeader()

                # Display the data for the specified page
                self.showPage(start_row, end_row)
            else:
                QMessageBox.warning(None, '系统提示', '超出页面范围！')
        else:
            QMessageBox.warning(None, '系统提示', '请输入数字！')
            
    def clearTableExceptHeader(self):
        self.ViewShowTable.clearContents()
        self.ViewShowTable.setRowCount(0)

    def master_checkbox_changed(self, state):
        if self.now_page != 1:
            length_page = len(self.fake_data) - (self.now_page - 1) * self.rows_per_page
            rows = min(self.rows_per_page, length_page)
        else:
            rows = min(self.rows_per_page, len(self.fake_data))
        for row in range(1, rows+1):  # 从第二行开始
            checkbox = self.ViewShowTable.cellWidget(row, 0)  # 获取复选框
            if state == 2:
                checkbox.setCheckState(Qt.CheckState.Checked)  # 设置为选中状态
            else:
                checkbox.setCheckState(Qt.CheckState.Unchecked)  # 设置为未选中状态

    def showPage(self, start_row, end_row):
        rows = self.rows_per_page
        columns = 13

        self.ViewShowTable.setRowCount(rows+1) 
        self.ViewShowTable.setColumnCount(columns)
        self.ViewShowTable.verticalHeader().setVisible(False)  # 隐藏垂直标题 序号

        self.master_checkbox = QCheckBox()  # 将 master_checkbox 存储为对象的属性
        self.master_checkbox.setStyleSheet("QCheckBox { padding-left: 10%; text-align: center;}")
        self.master_checkbox.stateChanged.connect(self.master_checkbox_changed)

        self.ViewShowTable.setCellWidget(0, 0, self.master_checkbox)  # 使用 self.master_checkbox

        # 设置居中和加粗的字体
        font = QFont()
        font.setBold(True)

        column_names = ["序号", "物料编码", "图纸号", "名称", "规格/型号", "材料", "颜色", "数量", "单位", "物料类别", "备注"]
        
        for col, text in enumerate(column_names, start=1):
            item = QTableWidgetItem(text)
            item.setFont(font)  # 设置字体为加粗
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中对齐
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
            self.ViewShowTable.setItem(0, col, item)

        for col in range(columns-1, columns):
            item = QTableWidgetItem("")
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # Set the cells to read-only
            self.ViewShowTable.setItem(0, col, item)

        # 隐藏原始的列名
        self.ViewShowTable.horizontalHeader().setVisible(False)

        rows = min(self.rows_per_page, end_row-start_row)

        for row in range(1, rows+1):  # 从第二行开始，添加序号
            item = QTableWidgetItem(str((self.now_page-1)*self.rows_per_page + row))  # 将行号作为文本创建一个表格项
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中对齐
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
            self.ViewShowTable.setItem(row, 1, item)  # 将表格项添加到第二列

        for row in range(1, self.rows_per_page + 1):  # 从第二行开始
            if row <= rows:
                # 显示的行
                for col in range(2, columns - 1):  # 从第三列开始
                    item = QTableWidgetItem(str(self.fake_data[row + start_row - 1][col]))  # 调整索引以匹配 fake_data 列表
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中对齐
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
                    self.ViewShowTable.setItem(row, col, item)  # 在表格中设置项目
            else:
                # 未显示的行
                for col in range(0, columns):
                    item = QTableWidgetItem("")  # 创建空项目
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
                    self.ViewShowTable.setItem(row, col, item)  # 在表格中设置项目


        # 在最后一列添加按钮
        for row in range(rows):
            checkbox = QCheckBox()  # 创建复选框
            checkbox.setStyleSheet("QCheckBox { padding-left: 10%; text-align: center;}")
            self.ViewShowTable.setCellWidget(row+1, 0, checkbox)  # 将复选框添加到表格的第一列
            self.edit_button = QPushButton("编辑")
            self.ViewShowTable.setCellWidget(row+1, columns-1, self.edit_button)  # 将编辑按钮添加到表格的最后一列

            # 添加编辑按钮点击事件
            # row_id = self.fake_data[(self.now_page - 1) * self.rows_per_page + row][0]
            # print(row_id)
            # self.edit_button.clicked.connect(lambda _, id=row_id: self.open_editList_window(id))

        self.ViewShowTable.setColumnWidth(0, 30)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(1, 35)  # Adjust the width of the "Save" button column
        self.ViewShowTable.setColumnWidth(2, 130)  # Adjust the width of the "View" button column
        self.ViewShowTable.setColumnWidth(3, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(4, 130)  # Adjust the width of the "Save" button column
        self.ViewShowTable.setColumnWidth(5, 130)  # Adjust the width of the "View" button column
        self.ViewShowTable.setColumnWidth(6, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(7, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(8, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(9, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(10, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(11, 130)  # Adjust the width of the "Edit" button column
        self.ViewShowTable.setColumnWidth(12, 45)  # Adjust the width of the "Edit" button column

        for row in range(self.rows_per_page + 1):
            self.ViewShowTable.setRowHeight(row,55)


    def initTable(self):
        self.clearTableExceptHeader()
        s_Name = self.searchLineEdit.text()

        result = viewDao.list(s_Name, self.row_id)

        if result:
            self.fake_data = result

        self.total_pages = (len(self.fake_data) + self.rows_per_page - 1) // self.rows_per_page

        # Check if the current page exceeds the total pages after the data deletion
        if self.now_page > self.total_pages:
            self.now_page = max(1, self.total_pages)  # Update the current page to the last page or the first page
            self.pageShowLabel.setText(f"第{self.now_page}页/共{self.total_pages}页")
        else:
            self.pageShowLabel.setText(f"第{self.now_page}页/共{self.total_pages}页")


        start_row = (self.now_page - 1) * self.rows_per_page
        end_row = min(self.now_page * self.rows_per_page, len(self.fake_data))

        self.showPage(start_row, end_row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ViewList()
    ui.show()

    sys.exit(app.exec())