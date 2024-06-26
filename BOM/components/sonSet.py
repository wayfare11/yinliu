# Form implementation generated from reading ui file 'd:\WorkSpace\PYQT_dev\BOM\view\sonSet.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QPushButton, QCheckBox, QMessageBox
from dao import mainListDao

class SonSet_widget(QWidget):
    def __init__(self, now_materialCode):
        self.now_materialCode = now_materialCode
        super(SonSet_widget, self).__init__()
        self.total_pages = 1  # 初始化总页数为1
        self.rows_per_page = 10
        self.now_page = 1
        self.fake_data = None
        self.setupUi(self)
        self.initTable()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.materialCodelabel = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.materialCodelabel.setFont(font)
        self.materialCodelabel.setObjectName("materialCodelabel")
        self.horizontalLayout.addWidget(self.materialCodelabel)

        # 设置当前物料编码
        self.materialCodelabel.setText(self.now_materialCode)

        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameSearchEdit = QtWidgets.QLineEdit(parent=Form)
        self.nameSearchEdit.setObjectName("nameSearchEdit")
        self.horizontalLayout_2.addWidget(self.nameSearchEdit)
        self.materialCodeSearchEdit = QtWidgets.QLineEdit(parent=Form)
        self.materialCodeSearchEdit.setObjectName("materialCodeSearchEdit")
        self.horizontalLayout_2.addWidget(self.materialCodeSearchEdit)
        self.searchButton = QtWidgets.QPushButton(parent=Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)

        # 绑定搜索按钮点击事件
        self.searchButton.clicked.connect(self.initTable)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.levelShowtable = QtWidgets.QTableWidget(parent=Form)
        self.levelShowtable.setObjectName("levelShowtable")
        self.levelShowtable.setColumnCount(0)
        self.levelShowtable.setRowCount(0)
        self.verticalLayout.addWidget(self.levelShowtable)

        # 设置表格数据随窗口大小变动
        self.levelShowtable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)  # 设置列的自动调整模式为拉伸
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pageShowBox = QtWidgets.QComboBox(parent=Form)
        self.pageShowBox.setObjectName("pageShowBox")
        self.pageShowBox.addItem("")
        self.pageShowBox.addItem("")
        self.pageShowBox.addItem("")
        self.pageShowBox.addItem("")
        self.horizontalLayout_3.addWidget(self.pageShowBox)

        self.pageShowBox.currentIndexChanged.connect(self.pageComboBoxChanged)

        self.pageShowlabel = QtWidgets.QLabel(parent=Form)
        self.pageShowlabel.setObjectName("pageShowlabel")
        self.horizontalLayout_3.addWidget(self.pageShowlabel)
        self.pageInputEdit = QtWidgets.QLineEdit(parent=Form)
        self.pageInputEdit.setObjectName("pageInputEdit")
        self.horizontalLayout_3.addWidget(self.pageInputEdit)
        self.gotoButton = QtWidgets.QPushButton(parent=Form)
        self.gotoButton.setObjectName("gotoButton")
        self.horizontalLayout_3.addWidget(self.gotoButton)

        # 新增前往按钮点击事件
        self.gotoButton.clicked.connect(self.goToButtonClicked)

        self.forwardButton = QtWidgets.QPushButton(parent=Form)
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout_3.addWidget(self.forwardButton)

        # 添加前一页按钮点击事件
        self.forwardButton.clicked.connect(self.forwardButtonClicked)

        self.nextButton = QtWidgets.QPushButton(parent=Form)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_3.addWidget(self.nextButton)

        # 添加后一页按钮点击事件
        self.nextButton.clicked.connect(self.nextButtonClicked)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.certainButton = QtWidgets.QPushButton(parent=Form)
        self.certainButton.setObjectName("certainButton")
        self.horizontalLayout_4.addWidget(self.certainButton)

        # 确定按钮点击事件
        self.certainButton.clicked.connect(self.checkCheckBoxes)

        self.cancelButton = QtWidgets.QPushButton(parent=Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)

        self.cancelButton.clicked.connect(self.closeNowWindow)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "sonSet"))
        self.label_3.setText(_translate("Form", "物料编码"))
        # self.materialCodelabel.setText(_translate("Form", "0000001"))
        self.label.setText(_translate("Form", "的子级"))
        self.nameSearchEdit.setPlaceholderText(_translate("Form", "请输入查询的名称"))
        self.materialCodeSearchEdit.setPlaceholderText(_translate("Form", "请输入查询的物料编码"))
        self.searchButton.setText(_translate("Form", "搜索"))
        self.pageShowBox.setItemText(0, _translate("Form", "每页显示10条"))
        self.pageShowBox.setItemText(1, _translate("Form", "每页显示20条"))
        self.pageShowBox.setItemText(2, _translate("Form", "每页显示50条"))
        self.pageShowBox.setItemText(3, _translate("Form", "每页显示100条"))
        self.pageShowlabel.setText(_translate("Form", "第1页/共1页"))
        self.pageInputEdit.setPlaceholderText(_translate("Form", "请输入要跳转的页码"))
        self.gotoButton.setText(_translate("Form", "前往"))
        self.forwardButton.setText(_translate("Form", "前一页"))
        self.nextButton.setText(_translate("Form", "后一页"))
        self.certainButton.setText(_translate("Form", "确定"))
        self.cancelButton.setText(_translate("Form", "取消"))

    def closeNowWindow(self):
        self.close()

    def checkCheckBoxes(self):

        now_son_data = mainListDao.list_son_set_by_id(self.now_materialCode)[0][11]

        # 获取当前页的起始行和结束行
        start_row = (self.now_page - 1) * self.rows_per_page
        end_row = min(self.now_page * self.rows_per_page, len(self.fake_data))

        # 遍历当前页的所有数据
        for row in range(start_row, end_row):
            checkbox = self.levelShowtable.cellWidget(row - start_row + 1, 0)  # 获取复选框
            current_id = self.fake_data[row][13]  # 获取当前行的数据
            if checkbox.isChecked():
                if not re.search(r'\b' + re.escape(current_id) + r'\b', now_son_data):
                    if now_son_data:
                        now_son_data += f",{current_id}"
                    else:
                        now_son_data = current_id
            else:
                if re.search(r'\b' + re.escape(current_id) + r'\b', now_son_data):
                    now_son_data = ",".join(filter(lambda x: x != current_id, now_son_data.split(",")))

        reply = QMessageBox.question(self, '确认', '确定要设置当前层级关系吗？', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        # 根据用户的选择执行相应的操作
        if reply == QMessageBox.StandardButton.Yes:
            if mainListDao.updateSonSet(now_son_data, self.now_materialCode) > 0:
                QMessageBox.information(None, '系统提示', '层级关系设置成功')
                self.close()
            else:
                QMessageBox.warning(None, '系统提示', '设置失败')

    def master_checkbox_changed(self, state):
        if self.now_page != 1:
            length_page = len(self.fake_data) - (self.now_page - 1) * self.rows_per_page
            rows = min(self.rows_per_page, length_page)
        else:
            rows = min(self.rows_per_page, len(self.fake_data))
        for row in range(1, rows+1):  # 从第二行开始
            checkbox = self.levelShowtable.cellWidget(row, 0)  # 获取复选框
            if state == 2:
                checkbox.setCheckState(Qt.CheckState.Checked)  # 设置为选中状态
            else:
                checkbox.setCheckState(Qt.CheckState.Unchecked)  # 设置为未选中状态

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
        self.pageInputEdit.setText("")
        self.initTable()

    def goToButtonClicked(self):
        # Get the input page number
        page_text = self.pageInputEdit.text()
        if page_text.isdigit():  # Check if the input is a number
            page_number = int(page_text)

            if 1 <= page_number <= self.total_pages:
                # Calculate the start and end rows for the specified page
                start_row = (page_number - 1) * self.rows_per_page
                end_row = min(page_number * self.rows_per_page, len(self.fake_data))

                self.now_page = page_number
                self.pageShowlabel.setText(f"第{self.now_page}页/共{self.total_pages}页")

                # Clear the table except for the header row before displaying the new data
                self.clearTableExceptHeader()

                # Display the data for the specified page
                self.showPage(start_row, end_row)
            else:
                QMessageBox.warning(None, '系统提示', '超出页面范围！')
        else:
            QMessageBox.warning(None, '系统提示', '请输入数字！')

    def forwardButtonClicked(self):
        if self.now_page > 1:  # 如果当前页不是第一页
            self.now_page -= 1  # 更新当前页数为上一页
            self.pageShowlabel.setText(f"第{self.now_page}页/共{self.total_pages}页")  # 更新页面标签显示
            start_row = (self.now_page - 1) * self.rows_per_page  # 计算起始行
            end_row = self.now_page * self.rows_per_page  # 计算结束行
            self.clearTableExceptHeader()  # 清空表格数据
            self.showPage(start_row, end_row)  # 显示上一页的数据
        # 如果当前页已经是第一页，则点击按钮时不执行任何操作
            
    def nextButtonClicked(self):
        if self.now_page < self.total_pages:  # 如果当前页不是最后一页
            self.now_page += 1  # 更新当前页数为下一页
            self.pageShowlabel.setText(f"第{self.now_page}页/共{self.total_pages}页")  # 更新页面标签显示
            start_row = (self.now_page - 1) * self.rows_per_page  # 计算起始行
            end_row = min(self.now_page * self.rows_per_page, len(self.fake_data))  # 计算结束行
            self.clearTableExceptHeader()  # 清空表格数据
            self.showPage(start_row, end_row)  # 显示下一页的数据
        # 如果当前页已经是最后一页，则点击按钮时不执行任何操作
            
    def clearTableExceptHeader(self):
        self.levelShowtable.clearContents()
        self.levelShowtable.setRowCount(0)

    def showPage(self, start_row, end_row):

        now_son_data = mainListDao.list_son_set_by_id(self.now_materialCode)[0][11]

        rows = self.rows_per_page
        columns = 13
        self.levelShowtable.setRowCount(rows+1) 
        self.levelShowtable.setColumnCount(columns)
        self.levelShowtable.verticalHeader().setVisible(False)  # 隐藏垂直标题 序号
        self.master_checkbox = QCheckBox()  # 将 master_checkbox 存储为对象的属性
        self.master_checkbox.setStyleSheet("QCheckBox { padding-left: 10%; text-align: center;}")
        self.master_checkbox.stateChanged.connect(self.master_checkbox_changed)

        self.levelShowtable.setCellWidget(0, 0, self.master_checkbox)  # 使用 self.master_checkbox

        # 设置居中和加粗的字体
        font = QFont()
        font.setBold(True)
        column_names = ["序号", "物料编码", "图纸号", "名称", "规格/型号", "材料", "颜色", "数量", "单位", "物料类别", "备注"]
        for col, text in enumerate(column_names, start=1):
            item = QTableWidgetItem(text)
            item.setFont(font)  # 设置字体为加粗
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中对齐
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
            self.levelShowtable.setItem(0, col, item)
        
        # 隐藏原始的列名
        self.levelShowtable.horizontalHeader().setVisible(False)

        rows = min(self.rows_per_page, end_row-start_row)

        for row in range(1, rows+1):  # 从第二行开始，添加序号
            item = QTableWidgetItem(str((self.now_page-1)*self.rows_per_page + row))  # 将行号作为文本创建一个表格项
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中对齐
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
            self.levelShowtable.setItem(row, 1, item)  # 将表格项添加到第二列

        for row in range(1, self.rows_per_page + 1):  # 从第二行开始，添加数据
            if row <= rows:
                # 显示的行
                for col in range(2, columns - 1):  # 从第三列开始
                    item = QTableWidgetItem(str(self.fake_data[row + start_row-1][col-12]))  # 调整索引以匹配 fake_data 列表
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置居中对齐
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
                    self.levelShowtable.setItem(row, col, item)  # 在表格中设置项目
            else:
                # 未显示的行
                for col in range(0, columns):
                    item = QTableWidgetItem("")  # 创建空项目
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # 设置单元格为只读
                    self.levelShowtable.setItem(row, col, item)  # 在表格中设置项目
        # 复选框初始化
        for row in range(rows):
            checkbox = QCheckBox()  # 创建复选框
            checkbox.setStyleSheet("QCheckBox { padding-left: 10%; text-align: center;}")
            self.levelShowtable.setCellWidget(row+1, 0, checkbox)  # 将复选框添加到表格的第一列

            now_row_son_id = self.fake_data[row + start_row][13]
            
            if re.search(r'\b' + re.escape(now_row_son_id) + r'\b', now_son_data):
                # 如果 now_row_son_id 存在于 now_son_data 中，并且满足正则表达式条件，执行相应的操作
                checkbox.setChecked(True)  # 


        # 第一列列宽固定
        self.levelShowtable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)  # 设置第一列的列宽模式为固定大小
        self.levelShowtable.setColumnWidth(0, 30)  # 设置第一列的宽度为30

        for row in range(1, self.rows_per_page + 1):
            self.levelShowtable.setRowHeight(row, 40)  # 设置行高为30像素

    def initTable(self):
        self.clearTableExceptHeader()

        self.fake_data = ""

        nameInput = self.nameSearchEdit.text()
        s_materialSearchCode = self.materialCodeSearchEdit.text()

        self.fake_data = mainListDao.list_son_set(self.now_materialCode, nameInput, s_materialSearchCode)

        self.total_pages = (len(self.fake_data) + self.rows_per_page - 1) // self.rows_per_page

        # Check if the current page exceeds the total pages after the data deletion
        if self.now_page > self.total_pages:
            self.now_page = max(1, self.total_pages)  # Update the current page to the last page or the first page
            self.pageShowlabel.setText(f"第{self.now_page}页/共{self.total_pages}页")
        else:
            self.pageShowlabel.setText(f"第{self.now_page}页/共{self.total_pages}页")

        start_row = (self.now_page - 1) * self.rows_per_page
        end_row = min(self.now_page * self.rows_per_page, len(self.fake_data))

        self.showPage(start_row, end_row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = SonSet_widget()
    ui.show()

    sys.exit(app.exec())