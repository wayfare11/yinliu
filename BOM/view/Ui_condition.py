# Form implementation generated from reading ui file 'd:\WorkSpace\PYQT_dev\BOM\view\condition.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 842)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.materialCodelabel = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.materialCodelabel.setFont(font)
        self.materialCodelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.materialCodelabel.setObjectName("materialCodelabel")
        self.horizontalLayout.addWidget(self.materialCodelabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DC_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.DC_checkBox.setObjectName("DC_checkBox")
        self.horizontalLayout_2.addWidget(self.DC_checkBox)
        self.BDC_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.BDC_checkBox.setObjectName("BDC_checkBox")
        self.horizontalLayout_2.addWidget(self.BDC_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 14, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 16, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dandao_T_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_T_checkBox.setObjectName("dandao_T_checkBox")
        self.horizontalLayout_7.addWidget(self.dandao_T_checkBox)
        self.dandao_TP_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_TP_checkBox.setObjectName("dandao_TP_checkBox")
        self.horizontalLayout_7.addWidget(self.dandao_TP_checkBox)
        self.dandao_SA_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_SA_checkBox.setObjectName("dandao_SA_checkBox")
        self.horizontalLayout_7.addWidget(self.dandao_SA_checkBox)
        self.dandao_SAP_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_SAP_checkBox.setObjectName("dandao_SAP_checkBox")
        self.horizontalLayout_7.addWidget(self.dandao_SAP_checkBox)
        self.dandao_SB_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_SB_checkBox.setObjectName("dandao_SB_checkBox")
        self.horizontalLayout_7.addWidget(self.dandao_SB_checkBox)
        self.dandao_SBP_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_SBP_checkBox.setObjectName("dandao_SBP_checkBox")
        self.horizontalLayout_7.addWidget(self.dandao_SBP_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_7, 13, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 18, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.yinliu_5F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_5F_checkBox.setObjectName("yinliu_5F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_5F_checkBox)
        self.yinliu_6F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_6F_checkBox.setObjectName("yinliu_6F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_6F_checkBox)
        self.yinliu_7F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_7F_checkBox.setObjectName("yinliu_7F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_7F_checkBox)
        self.yinliu_8F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_8F_checkBox.setObjectName("yinliu_8F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_8F_checkBox)
        self.yinliu_10F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_10F_checkBox.setObjectName("yinliu_10F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_10F_checkBox)
        self.yinliu_12F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_12F_checkBox.setObjectName("yinliu_12F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_12F_checkBox)
        self.yinliu_14F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_14F_checkBox.setObjectName("yinliu_14F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_14F_checkBox)
        self.yinliu_16F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_16F_checkBox.setObjectName("yinliu_16F_checkBox")
        self.horizontalLayout_8.addWidget(self.yinliu_16F_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 15, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 22, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.yinliu_20cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_20cm_checkBox.setObjectName("yinliu_20cm_checkBox")
        self.horizontalLayout_9.addWidget(self.yinliu_20cm_checkBox)
        self.yinliu_25cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_25cm_checkBox.setObjectName("yinliu_25cm_checkBox")
        self.horizontalLayout_9.addWidget(self.yinliu_25cm_checkBox)
        self.yinliu_30cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_30cm_checkBox.setObjectName("yinliu_30cm_checkBox")
        self.horizontalLayout_9.addWidget(self.yinliu_30cm_checkBox)
        self.yinliu_35cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_35cm_checkBox.setObjectName("yinliu_35cm_checkBox")
        self.horizontalLayout_9.addWidget(self.yinliu_35cm_checkBox)
        self.yinliu_40cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_40cm_checkBox.setObjectName("yinliu_40cm_checkBox")
        self.horizontalLayout_9.addWidget(self.yinliu_40cm_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_9, 17, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dandao_L_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_L_checkBox.setObjectName("dandao_L_checkBox")
        self.horizontalLayout_6.addWidget(self.dandao_L_checkBox)
        self.dandao_N_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_N_checkBox.setObjectName("dandao_N_checkBox")
        self.horizontalLayout_6.addWidget(self.dandao_N_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_6, 11, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.yinliu_J_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_J_checkBox.setObjectName("yinliu_J_checkBox")
        self.horizontalLayout_11.addWidget(self.yinliu_J_checkBox)
        self.yinliu_P_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_P_checkBox.setObjectName("yinliu_P_checkBox")
        self.horizontalLayout_11.addWidget(self.yinliu_P_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_11, 21, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dandao_inner_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_inner_checkBox.setObjectName("dandao_inner_checkBox")
        self.horizontalLayout_5.addWidget(self.dandao_inner_checkBox)
        self.dandao_outer_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_outer_checkBox.setObjectName("dandao_outer_checkBox")
        self.horizontalLayout_5.addWidget(self.dandao_outer_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dandao_6F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_6F_checkBox.setObjectName("dandao_6F_checkBox")
        self.horizontalLayout_3.addWidget(self.dandao_6F_checkBox)
        self.dandao_7F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_7F_checkBox.setObjectName("dandao_7F_checkBox")
        self.horizontalLayout_3.addWidget(self.dandao_7F_checkBox)
        self.dandao_8F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_8F_checkBox.setObjectName("dandao_8F_checkBox")
        self.horizontalLayout_3.addWidget(self.dandao_8F_checkBox)
        self.dandao_10F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_10F_checkBox.setObjectName("dandao_10F_checkBox")
        self.horizontalLayout_3.addWidget(self.dandao_10F_checkBox)
        self.dandao_12F_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_12F_checkBox.setObjectName("dandao_12F_checkBox")
        self.horizontalLayout_3.addWidget(self.dandao_12F_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dandao_25cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_25cm_checkBox.setObjectName("dandao_25cm_checkBox")
        self.horizontalLayout_4.addWidget(self.dandao_25cm_checkBox)
        self.dandao_30cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_30cm_checkBox.setObjectName("dandao_30cm_checkBox")
        self.horizontalLayout_4.addWidget(self.dandao_30cm_checkBox)
        self.dandao_35cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_35cm_checkBox.setObjectName("dandao_35cm_checkBox")
        self.horizontalLayout_4.addWidget(self.dandao_35cm_checkBox)
        self.dandao_40cm_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.dandao_40cm_checkBox.setObjectName("dandao_40cm_checkBox")
        self.horizontalLayout_4.addWidget(self.dandao_40cm_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.yinliu_T_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_T_checkBox.setObjectName("yinliu_T_checkBox")
        self.horizontalLayout_14.addWidget(self.yinliu_T_checkBox)
        self.yinliu_TP_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_TP_checkBox.setObjectName("yinliu_TP_checkBox")
        self.horizontalLayout_14.addWidget(self.yinliu_TP_checkBox)
        self.yinliu_SA_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_SA_checkBox.setObjectName("yinliu_SA_checkBox")
        self.horizontalLayout_14.addWidget(self.yinliu_SA_checkBox)
        self.yinliu_SAP_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_SAP_checkBox.setObjectName("yinliu_SAP_checkBox")
        self.horizontalLayout_14.addWidget(self.yinliu_SAP_checkBox)
        self.yinliu_SB_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_SB_checkBox.setObjectName("yinliu_SB_checkBox")
        self.horizontalLayout_14.addWidget(self.yinliu_SB_checkBox)
        self.yinliu_SBP_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_SBP_checkBox.setObjectName("yinliu_SBP_checkBox")
        self.horizontalLayout_14.addWidget(self.yinliu_SBP_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_14, 23, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.yinliu_L_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_L_checkBox.setObjectName("yinliu_L_checkBox")
        self.horizontalLayout_10.addWidget(self.yinliu_L_checkBox)
        self.yinliu_N_checkBox = QtWidgets.QCheckBox(parent=Form)
        self.yinliu_N_checkBox.setObjectName("yinliu_N_checkBox")
        self.horizontalLayout_10.addWidget(self.yinliu_N_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_10, 19, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 20, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-top: 0.5px solid grey;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.materialCodeSetlabel = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materialCodeSetlabel.setFont(font)
        self.materialCodeSetlabel.setText("")
        self.materialCodeSetlabel.setObjectName("materialCodeSetlabel")
        self.horizontalLayout_12.addWidget(self.materialCodeSetlabel)
        self.horizontalLayout_12.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.certainButton = QtWidgets.QPushButton(parent=Form)
        self.certainButton.setObjectName("certainButton")
        self.horizontalLayout_15.addWidget(self.certainButton)
        self.cancelButton = QtWidgets.QPushButton(parent=Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_15.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Condition"))
        self.materialCodelabel.setText(_translate("Form", "查询条件设置"))
        self.DC_checkBox.setText(_translate("Form", "DC"))
        self.BDC_checkBox.setText(_translate("Form", "BDC"))
        self.label_4.setText(_translate("Form", "胆道-长度"))
        self.label_8.setText(_translate("Form", "引流-直径"))
        self.label_9.setText(_translate("Form", "引流-长度"))
        self.dandao_T_checkBox.setText(_translate("Form", "T型"))
        self.dandao_TP_checkBox.setText(_translate("Form", "TP型"))
        self.dandao_SA_checkBox.setText(_translate("Form", "SA型"))
        self.dandao_SAP_checkBox.setText(_translate("Form", "SAP型"))
        self.dandao_SB_checkBox.setText(_translate("Form", "SB型"))
        self.dandao_SBP_checkBox.setText(_translate("Form", "SBP型"))
        self.label_10.setText(_translate("Form", "引流-锁定形式"))
        self.yinliu_5F_checkBox.setText(_translate("Form", "5F"))
        self.yinliu_6F_checkBox.setText(_translate("Form", "6F"))
        self.yinliu_7F_checkBox.setText(_translate("Form", "7F"))
        self.yinliu_8F_checkBox.setText(_translate("Form", "8F"))
        self.yinliu_10F_checkBox.setText(_translate("Form", "10F"))
        self.yinliu_12F_checkBox.setText(_translate("Form", "12F"))
        self.yinliu_14F_checkBox.setText(_translate("Form", "14F"))
        self.yinliu_16F_checkBox.setText(_translate("Form", "16F"))
        self.label_12.setText(_translate("Form", "引流-配置代号"))
        self.yinliu_20cm_checkBox.setText(_translate("Form", "20cm"))
        self.yinliu_25cm_checkBox.setText(_translate("Form", "25cm"))
        self.yinliu_30cm_checkBox.setText(_translate("Form", "30cm"))
        self.yinliu_35cm_checkBox.setText(_translate("Form", "35cm"))
        self.yinliu_40cm_checkBox.setText(_translate("Form", "40cm"))
        self.dandao_L_checkBox.setText(_translate("Form", "L:可锁定猪尾型"))
        self.dandao_N_checkBox.setText(_translate("Form", "N:非锁定猪尾型"))
        self.yinliu_J_checkBox.setText(_translate("Form", "J:J型"))
        self.yinliu_P_checkBox.setText(_translate("Form", "P:猪尾型"))
        self.dandao_inner_checkBox.setText(_translate("Form", "无内容:内外引流"))
        self.dandao_outer_checkBox.setText(_translate("Form", "W:外引流"))
        self.dandao_6F_checkBox.setText(_translate("Form", "6F"))
        self.dandao_7F_checkBox.setText(_translate("Form", "7F"))
        self.dandao_8F_checkBox.setText(_translate("Form", "8F"))
        self.dandao_10F_checkBox.setText(_translate("Form", "10F"))
        self.dandao_12F_checkBox.setText(_translate("Form", "12F"))
        self.label_7.setText(_translate("Form", "胆道-配置代号"))
        self.label_6.setText(_translate("Form", "胆道-头端样式"))
        self.label_3.setText(_translate("Form", "胆道-直径"))
        self.dandao_25cm_checkBox.setText(_translate("Form", "25cm"))
        self.dandao_30cm_checkBox.setText(_translate("Form", "30cm"))
        self.dandao_35cm_checkBox.setText(_translate("Form", "35cm"))
        self.dandao_40cm_checkBox.setText(_translate("Form", "40cm"))
        self.yinliu_T_checkBox.setText(_translate("Form", "T型"))
        self.yinliu_TP_checkBox.setText(_translate("Form", "TP型"))
        self.yinliu_SA_checkBox.setText(_translate("Form", "SA型"))
        self.yinliu_SAP_checkBox.setText(_translate("Form", "SAP型"))
        self.yinliu_SB_checkBox.setText(_translate("Form", "SB型"))
        self.yinliu_SBP_checkBox.setText(_translate("Form", "SBP型"))
        self.yinliu_L_checkBox.setText(_translate("Form", "L:可锁定型"))
        self.yinliu_N_checkBox.setText(_translate("Form", "N:非锁定型"))
        self.label_11.setText(_translate("Form", "引流-头端样式"))
        self.label_2.setText(_translate("Form", "产品代号"))
        self.label_5.setText(_translate("Form", "胆道-引流方式"))
        self.label.setText(_translate("Form", "当前零部件的物料编码："))
        self.certainButton.setText(_translate("Form", "确定"))
        self.cancelButton.setText(_translate("Form", "取消"))