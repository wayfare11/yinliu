# Form implementation generated from reading ui file 'd:\WorkSpace\PYQT_dev\yinliu\view\customAdd.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 596)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 90, 441, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(30, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.materialCodeBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materialCodeBox.setFont(font)
        self.materialCodeBox.setEditable(True)
        self.materialCodeBox.setObjectName("materialCodeBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.materialCodeBox)
        self.Label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_2.setFont(font)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_2)
        self.drawingCodeBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.drawingCodeBox.setFont(font)
        self.drawingCodeBox.setEditable(True)
        self.drawingCodeBox.setObjectName("drawingCodeBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.drawingCodeBox)
        self.Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label.setFont(font)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label)
        self.NameBox_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameBox_2.setFont(font)
        self.NameBox_2.setEditable(True)
        self.NameBox_2.setObjectName("NameBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NameBox_2)
        self.Label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_3.setFont(font)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_3)
        self.SizeBox_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SizeBox_3.setFont(font)
        self.SizeBox_3.setEditable(True)
        self.SizeBox_3.setObjectName("SizeBox_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SizeBox_3)
        self.Label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_4.setFont(font)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_4)
        self.materialBox_4 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materialBox_4.setFont(font)
        self.materialBox_4.setEditable(True)
        self.materialBox_4.setObjectName("materialBox_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.materialBox_4)
        self.Label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_5.setFont(font)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_5)
        self.ColorBox_5 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ColorBox_5.setFont(font)
        self.ColorBox_5.setEditable(True)
        self.ColorBox_5.setObjectName("ColorBox_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ColorBox_5)
        self.Label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_6.setFont(font)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_6)
        self.NumberBox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumberBox.setFont(font)
        self.NumberBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumberBox.setObjectName("NumberBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NumberBox)
        self.Label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_7.setFont(font)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_7)
        self.unitBox_6 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unitBox_6.setFont(font)
        self.unitBox_6.setObjectName("unitBox_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.unitBox_6)
        self.Label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_8.setFont(font)
        self.Label_8.setObjectName("Label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_8)
        self.categoryBox_7 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryBox_7.setFont(font)
        self.categoryBox_7.setObjectName("categoryBox_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.categoryBox_7)
        self.Label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_9.setFont(font)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Label_9)
        self.noteEdit = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noteEdit.setFont(font)
        self.noteEdit.setObjectName("noteEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.noteEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 510, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.certainButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.certainButton.setObjectName("certainButton")
        self.horizontalLayout.addWidget(self.certainButton)
        self.cancelButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.cancelButton_2.setObjectName("cancelButton_2")
        self.horizontalLayout.addWidget(self.cancelButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "自定义新增"))
        self.label_2.setText(_translate("Form", "物料编码"))
        self.Label_2.setText(_translate("Form", "图纸号"))
        self.Label.setText(_translate("Form", "名称"))
        self.Label_3.setText(_translate("Form", "规格/型号"))
        self.Label_4.setText(_translate("Form", "材料"))
        self.Label_5.setText(_translate("Form", "颜色"))
        self.Label_6.setText(_translate("Form", "数量"))
        self.Label_7.setText(_translate("Form", "单位"))
        self.Label_8.setText(_translate("Form", "物料类别"))
        self.Label_9.setText(_translate("Form", "备注"))
        self.certainButton.setText(_translate("Form", "确定"))
        self.cancelButton_2.setText(_translate("Form", "取消"))
