# Form implementation generated from reading ui file 'd:\WorkSpace\PYQT_dev\BOM\view\components.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchNameEdit = QtWidgets.QLineEdit(parent=Form)
        self.searchNameEdit.setObjectName("searchNameEdit")
        self.horizontalLayout_2.addWidget(self.searchNameEdit)
        self.searchButton = QtWidgets.QPushButton(parent=Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.addButton = QtWidgets.QPushButton(parent=Form)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(parent=Form)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.componentTable = QtWidgets.QTableWidget(parent=Form)
        self.componentTable.setObjectName("componentTable")
        self.componentTable.setColumnCount(0)
        self.componentTable.setRowCount(0)
        self.verticalLayout.addWidget(self.componentTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pageSelectBox = QtWidgets.QComboBox(parent=Form)
        self.pageSelectBox.setObjectName("pageSelectBox")
        self.pageSelectBox.addItem("")
        self.pageSelectBox.addItem("")
        self.pageSelectBox.addItem("")
        self.pageSelectBox.addItem("")
        self.horizontalLayout_3.addWidget(self.pageSelectBox)
        self.pageShowlabel = QtWidgets.QLabel(parent=Form)
        self.pageShowlabel.setObjectName("pageShowlabel")
        self.horizontalLayout_3.addWidget(self.pageShowlabel)
        self.pageInputEdit = QtWidgets.QLineEdit(parent=Form)
        self.pageInputEdit.setObjectName("pageInputEdit")
        self.horizontalLayout_3.addWidget(self.pageInputEdit)
        self.goToButton = QtWidgets.QPushButton(parent=Form)
        self.goToButton.setObjectName("goToButton")
        self.horizontalLayout_3.addWidget(self.goToButton)
        self.forwardButton = QtWidgets.QPushButton(parent=Form)
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout_3.addWidget(self.forwardButton)
        self.nextButton = QtWidgets.QPushButton(parent=Form)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_3.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Components"))
        self.label.setText(_translate("Form", "零部件物料库"))
        self.searchNameEdit.setPlaceholderText(_translate("Form", "请输入查询的名称"))
        self.searchButton.setText(_translate("Form", "搜索"))
        self.addButton.setText(_translate("Form", "新增"))
        self.deleteButton.setText(_translate("Form", "删除"))
        self.pageSelectBox.setItemText(0, _translate("Form", "每页10条"))
        self.pageSelectBox.setItemText(1, _translate("Form", "每页20条"))
        self.pageSelectBox.setItemText(2, _translate("Form", "每页50条"))
        self.pageSelectBox.setItemText(3, _translate("Form", "每页100条"))
        self.pageShowlabel.setText(_translate("Form", "第1页/共1页"))
        self.pageInputEdit.setPlaceholderText(_translate("Form", "请输入页数"))
        self.goToButton.setText(_translate("Form", "前往"))
        self.forwardButton.setText(_translate("Form", "前一页"))
        self.nextButton.setText(_translate("Form", "后一页"))
