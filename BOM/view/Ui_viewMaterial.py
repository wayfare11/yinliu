# Form implementation generated from reading ui file 'd:\WorkSpace\PYQT_dev\BOM\view\viewMaterial.ui'
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
        self.materialCodelabel = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.materialCodelabel.setFont(font)
        self.materialCodelabel.setText("")
        self.materialCodelabel.setObjectName("materialCodelabel")
        self.horizontalLayout.addWidget(self.materialCodelabel)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameSearchEdit = QtWidgets.QLineEdit(parent=Form)
        self.nameSearchEdit.setObjectName("nameSearchEdit")
        self.horizontalLayout_2.addWidget(self.nameSearchEdit)
        self.classSearchBox = QtWidgets.QComboBox(parent=Form)
        self.classSearchBox.setObjectName("classSearchBox")
        self.classSearchBox.addItem("")
        self.classSearchBox.addItem("")
        self.classSearchBox.addItem("")
        self.classSearchBox.addItem("")
        self.horizontalLayout_2.addWidget(self.classSearchBox)
        self.searchButton = QtWidgets.QPushButton(parent=Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.componentTable = QtWidgets.QTableWidget(parent=Form)
        self.componentTable.setObjectName("componentTable")
        self.componentTable.setColumnCount(0)
        self.componentTable.setRowCount(0)
        self.verticalLayout.addWidget(self.componentTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pageShowBox = QtWidgets.QComboBox(parent=Form)
        self.pageShowBox.setObjectName("pageShowBox")
        self.pageShowBox.addItem("")
        self.pageShowBox.addItem("")
        self.pageShowBox.addItem("")
        self.pageShowBox.addItem("")
        self.horizontalLayout_3.addWidget(self.pageShowBox)
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
        Form.setWindowTitle(_translate("Form", "viewMaterial"))
        self.label.setText(_translate("Form", "物料编码："))
        self.label_3.setText(_translate("Form", "零部件清单"))
        self.nameSearchEdit.setPlaceholderText(_translate("Form", "请输入名称"))
        self.classSearchBox.setItemText(0, _translate("Form", "请选择类别"))
        self.classSearchBox.setItemText(1, _translate("Form", "主料"))
        self.classSearchBox.setItemText(2, _translate("Form", "辅材"))
        self.classSearchBox.setItemText(3, _translate("Form", "包材"))
        self.searchButton.setText(_translate("Form", "搜索"))
        self.pageShowBox.setItemText(0, _translate("Form", "每页显示10条"))
        self.pageShowBox.setItemText(1, _translate("Form", "每页显示20条"))
        self.pageShowBox.setItemText(2, _translate("Form", "每页显示50条"))
        self.pageShowBox.setItemText(3, _translate("Form", "每页显示100条"))
        self.pageShowlabel.setText(_translate("Form", "第1页/共1页"))
        self.pageInputEdit.setPlaceholderText(_translate("Form", "请输入跳转的页码"))
        self.goToButton.setText(_translate("Form", "前往"))
        self.forwardButton.setText(_translate("Form", "前一页"))
        self.nextButton.setText(_translate("Form", "后一页"))
