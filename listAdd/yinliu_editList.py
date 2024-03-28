# Form implementation generated from reading ui file 'c:\Users\WB-wangyu\Desktop\文档\开发文档\DrainageTube\view\editList.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from entity.ListModel import ListType
from dao import listDao
from signal_update.signalsUpdate import global_signals

class EditItemList(QWidget):

    def __init__(self, row_id):
        super(EditItemList, self).__init__()
        self.row_id = row_id
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.searchData()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 592)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 80, 421, 461))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setContentsMargins(20, 0, 20, 0)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.listNameBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.listNameBox.setEditable(True)
        self.listNameBox.setObjectName("listNameBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.listNameBox)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.fileNumBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.fileNumBox.setEditable(True)
        self.fileNumBox.setObjectName("fileNumBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fileNumBox)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.versionNumBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.versionNumBox.setEditable(True)
        self.versionNumBox.setObjectName("versionNumBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.versionNumBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.productSpecificationLine = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.productSpecificationLine.setReadOnly(True)
        self.productSpecificationLine.setObjectName("productSpecificationLine")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.productSpecificationLine)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.productCodeBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.productCodeBox.setEditable(True)
        self.productCodeBox.lineEdit().setReadOnly(True)
        self.productCodeBox.setObjectName("productCodeBox")
        self.productCodeBox.addItem("1")
        self.productCodeBox.addItem("2")        
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.productCodeBox)

        # 添加点击事件，根据productCodeBox的选择来切换stackedWidget的页面
        self.productCodeBox.currentTextChanged.connect(self.onProductCodeChanged)

        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.formLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.page)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 371, 151))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_6.setContentsMargins(20, 0, 20, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.danDaoDimensionBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.danDaoDimensionBox.setEditable(True)
        self.danDaoDimensionBox.setObjectName("danDaoDimensionBox")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.danDaoDimensionBox)

        # danDaoDimensionBox有文本输入，就更新productSpecificationLine
        self.danDaoDimensionBox.currentTextChanged.connect(self.updateProductSpecification_dandao)

        self.danDaoStyleBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.danDaoStyleBox.setEditable(True)
        self.danDaoStyleBox.setObjectName("danDaoStyleBox")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.danDaoStyleBox)


        # danDaoStyleBox有文本输入，就更新productSpecificationLine
        self.danDaoStyleBox.currentTextChanged.connect(self.updateProductSpecification_dandao)

        self.danDaoConfigurationBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.danDaoConfigurationBox.setEditable(True)
        self.danDaoConfigurationBox.setObjectName("danDaoConfigurationBox")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.danDaoConfigurationBox)

        # danDaoConfigurationBox有文本输入，就更新productSpecificationLine
        self.danDaoConfigurationBox.currentTextChanged.connect(self.updateProductSpecification_dandao)

        self.label_8 = QtWidgets.QLabel(parent=self.page)
        self.label_8.setGeometry(QtCore.QRect(140, 10, 101, 18))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.page_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 371, 126))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_5.setContentsMargins(20, 0, 20, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_13 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.yinLiuDimensionBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.yinLiuDimensionBox.setEditable(True)
        self.yinLiuDimensionBox.setObjectName("yinLiuDimensionBox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yinLiuDimensionBox)

        # yinLiuDimensionBox有文本输入，就更新productSpecificationLine
        self.yinLiuDimensionBox.currentTextChanged.connect(self.updateProductSpecification_yinliu)

        self.label_14 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.yinLiuLockedBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.yinLiuLockedBox.setEditable(True)
        self.yinLiuLockedBox.setObjectName("yinLiuLockedBox")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yinLiuLockedBox)

        # yinLiuLockedBox有文本输入，就更新productSpecificationLine
        self.yinLiuLockedBox.currentTextChanged.connect(self.updateProductSpecification_yinliu)

        self.label_15 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.yinLiuStyleBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.yinLiuStyleBox.setEditable(True)
        self.yinLiuStyleBox.setObjectName("yinLiuStyleBox")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yinLiuStyleBox)

        # yinLiuStyleBox有文本输入，就更新productSpecificationLine
        self.yinLiuStyleBox.currentTextChanged.connect(self.updateProductSpecification_yinliu)

        self.label_16 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.yinLiuConfigurationBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.yinLiuConfigurationBox.setEditable(True)
        self.yinLiuConfigurationBox.setObjectName("yinLiuConfigurationBox")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yinLiuConfigurationBox)

        # yinLiuConfigurationBox有文本输入，就更新productSpecificationLine
        self.yinLiuConfigurationBox.currentTextChanged.connect(self.updateProductSpecification_yinliu)

        self.label_12 = QtWidgets.QLabel(parent=self.page_2)
        self.label_12.setGeometry(QtCore.QRect(140, 10, 111, 16))
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.page_2)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.stackedWidget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem1)
        self.label_17 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.dimensions = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.dimensions.setEditable(True)
        self.dimensions.setObjectName("dimensions")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dimensions)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.certainButton = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.certainButton.setObjectName("certainButton")
        self.horizontalLayout_2.addWidget(self.certainButton)

        # 点击确定实现新增
        self.certainButton.clicked.connect(self.edit_start)

        self.cancelButton_2 = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.cancelButton_2.setObjectName("cancelButton_2")
        self.horizontalLayout_2.addWidget(self.cancelButton_2)

        # 点击取消关闭当前窗口
        self.cancelButton_2.clicked.connect(Form.close)

        self.horizontalLayout_2.setStretch(0, 1)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "editList"))
        self.label_2.setText(_translate("Form", "名称"))
        self.label_3.setText(_translate("Form", "文件编号"))
        self.label_4.setText(_translate("Form", "版本号"))
        self.label_5.setText(_translate("Form", "产品规格"))
        self.label_6.setText(_translate("Form", "产品代号"))
        self.label_7.setText(_translate("Form", "规格尺寸"))
        self.label_9.setText(_translate("Form", "头端样式"))
        self.label_10.setText(_translate("Form", "配置代号"))
        self.label_8.setText(_translate("Form", "胆道引流导管"))
        self.label_13.setText(_translate("Form", "规格尺寸"))
        self.label_14.setText(_translate("Form", "锁定形式"))
        self.label_15.setText(_translate("Form", "头端样式"))
        self.label_16.setText(_translate("Form", "配置代号"))
        self.label_12.setText(_translate("Form", "引流导管套装"))
        self.label_17.setText(_translate("Form", "物料编码"))
        self.certainButton.setText(_translate("Form", "确定"))
        self.cancelButton_2.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "编辑清单"))

    def edit_start(self):
        a_Name = self.listNameBox.currentText()
        a_FileCode = self.fileNumBox.currentText()
        a_VersionCode = self.versionNumBox.currentText()
        a_ProductSize = self.productSpecificationLine.text()
        a_ProductCode = self.productCodeBox.currentText()
        a_DandaoSize = self.danDaoDimensionBox.currentText()
        a_DandaoStyle = self.danDaoStyleBox.currentText()
        a_DandaoCode = self.danDaoConfigurationBox.currentText()
        a_YinliuSize = self.yinLiuDimensionBox.currentText()
        a_YinliuLock = self.yinLiuLockedBox.currentText()
        a_YinliuStyle = self.yinLiuStyleBox.currentText()
        a_YinLiuConfigurationBox = self.yinLiuConfigurationBox.currentText()
        a_MaterialCode = self.dimensions.currentText()

        # 首先判定不能为空
        if a_Name.strip() == "":
            QMessageBox.warning(None, '系统提示', '名称不能为空！')
        elif  a_FileCode == "":
            QMessageBox.warning(None, '系统提示', '文件编号不能为空！')
        elif  a_VersionCode == "":
            QMessageBox.warning(None, '系统提示', '版本号不能为空！')

        elif a_ProductCode == "1":
            if a_DandaoSize.strip() == "":
                QMessageBox.warning(None, '系统提示', '规格尺寸不能为空！')
            elif a_DandaoStyle.strip() == "":
                QMessageBox.warning(None, '系统提示', '头端样式不能为空！')
            elif a_DandaoCode.strip() == "":
                QMessageBox.warning(None, '系统提示', '配置代号不能为空！')
            elif a_MaterialCode.strip() == "":
                QMessageBox.warning(None, '系统提示', '物料编码不能为空！')
            else:
                a_YinliuSize = ""
                a_YinliuLock = ""
                a_YinliuStyle = ""
                a_YinLiuConfigurationBox = ""

                listType = ListType(a_Name, a_FileCode, a_VersionCode, a_ProductSize, a_ProductCode, a_DandaoSize, a_DandaoStyle, a_DandaoCode, a_YinliuSize, a_YinliuLock, a_YinliuStyle, a_YinLiuConfigurationBox, a_MaterialCode)
                if listDao.update(listType, self.row_id) > 0:
                    QMessageBox.information(None, '系统提示', '修改成功')
                    self.close()
                    global_signals.updateTable.emit()
                else:
                    QMessageBox.warning(None, '系统提示', '修改失败')

        elif a_ProductCode == "2":
            if a_YinliuSize.strip() == "":
                QMessageBox.warning(None, '系统提示', '规格尺寸不能为空！')
            elif a_YinliuLock.strip() == "":
                QMessageBox.warning(None, '系统提示', '锁定形式不能为空！')
            elif a_YinliuStyle.strip() == "":
                QMessageBox.warning(None, '系统提示', '头端样式不能为空！')
            elif a_YinLiuConfigurationBox.strip() == "":
                QMessageBox.warning(None, '系统提示', '配置代号不能为空！')
            elif a_MaterialCode.strip() == "":
                QMessageBox.warning(None, '系统提示', '物料编码不能为空！')
            else:
                a_DandaoSize = ""
                a_DandaoStyle = ""
                a_DandaoCode = ""

                listType = ListType(a_Name, a_FileCode, a_VersionCode, a_ProductSize, a_ProductCode, a_DandaoSize, a_DandaoStyle, a_DandaoCode, a_YinliuSize, a_YinliuLock, a_YinliuStyle, a_YinLiuConfigurationBox, a_MaterialCode)
                if listDao.update(listType, self.row_id) > 0:
                    QMessageBox.information(None, '系统提示', '修改成功')
                    self.close()
                    global_signals.updateTable.emit()
                else:
                    QMessageBox.warning(None, '系统提示', '修改失败') 

    def searchData(self):
        data = listDao.searchById(self.row_id)
        data_Name = data[0][1]
        data_fileNum = data[0][2]
        data_versionNum = data[0][3]
        data_productSpecification = data[0][4]
        data_productCode = data[0][5]
        data_danDaoDimension = data[0][6]
        data_danDaoStyle = data[0][7]
        data_danDaoConfiguration = data[0][8]
        data_yinLiuDimension = data[0][9]
        data_yinLiuLocked = data[0][10]
        data_yinLiuStyle = data[0][11]
        data_yinLiuConfiguration = data[0][12]
        data_dimensions = data[0][13]

        self.listNameBox.setCurrentText(data_Name)
        self.fileNumBox.setCurrentText(data_fileNum)
        self.versionNumBox.setCurrentText(data_versionNum)
        self.productSpecificationLine.setText(data_productSpecification)
        self.productCodeBox.setCurrentText(data_productCode)
        self.danDaoDimensionBox.setCurrentText(data_danDaoDimension)
        self.danDaoStyleBox.setCurrentText(data_danDaoStyle)
        self.danDaoConfigurationBox.setCurrentText(data_danDaoConfiguration)
        self.yinLiuDimensionBox.setCurrentText(data_yinLiuDimension)
        self.yinLiuLockedBox.setCurrentText(data_yinLiuLocked)
        self.yinLiuStyleBox.setCurrentText(data_yinLiuStyle)
        self.yinLiuConfigurationBox.setCurrentText(data_yinLiuConfiguration)
        self.dimensions.setCurrentText(data_dimensions)


    def onProductCodeChanged(self, text):
        if text == "1":
            self.stackedWidget.setCurrentIndex(0)  # 显示第一页
            self.productSpecificationLine.setText("")
        elif text == "2":
            self.stackedWidget.setCurrentIndex(1)  # 显示第二页
            self.productSpecificationLine.setText("")
            
    def updateProductSpecification_dandao(self):
        # 获取这三个下拉框的当前文本值
        a_ProductCode = self.productCodeBox.currentText()
        a_DandaoSize = self.danDaoDimensionBox.currentText()
        a_DandaoStyle = self.danDaoStyleBox.currentText()
        a_DandaoCode = self.danDaoConfigurationBox.currentText()

        # 合并字符串并更新productSpecificationLine
        a_ProductSize = a_ProductCode + a_DandaoSize + a_DandaoStyle + a_DandaoCode
        self.productSpecificationLine.setText(a_ProductSize)

    def updateProductSpecification_yinliu(self):
        # 获取这三个下拉框的当前文本值
        a_ProductCode = self.productCodeBox.currentText()
        a_yinLiuDimensionBox = self.yinLiuDimensionBox.currentText()
        a_yinLiuLockedBox = self.yinLiuLockedBox.currentText()
        a_yinLiuStyleBox = self.yinLiuStyleBox.currentText()
        a_yinLiuConfigurationBox = self.yinLiuConfigurationBox.currentText()

        # 合并字符串并更新productSpecificationLine
        a_ProductSize = a_ProductCode + a_yinLiuDimensionBox + a_yinLiuLockedBox + a_yinLiuStyleBox + a_yinLiuConfigurationBox
        self.productSpecificationLine.setText(a_ProductSize)            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = EditItemList()
    ui.show()

    sys.exit(app.exec())