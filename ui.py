# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(791, 578)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.spinBox_impedance = QtWidgets.QSpinBox(self.tab)
        self.spinBox_impedance.setGeometry(QtCore.QRect(60, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_impedance.setFont(font)
        self.spinBox_impedance.setObjectName("spinBox_impedance")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(60, 320, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(40, 60, 267, 218))
        self.widget.setMinimumSize(QtCore.QSize(60, 0))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_color1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_color1.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_color1.setFont(font)
        self.pushButton_color1.setText("")
        self.pushButton_color1.setObjectName("pushButton_color1")
        self.gridLayout_2.addWidget(self.pushButton_color1, 0, 0, 1, 1)
        self.spinBox_thickness1 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thickness1.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_thickness1.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_thickness1.setFont(font)
        self.spinBox_thickness1.setProperty("value", 2)
        self.spinBox_thickness1.setObjectName("spinBox_thickness1")
        self.gridLayout_2.addWidget(self.spinBox_thickness1, 0, 1, 1, 1)
        self.comboBox_linetype1 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_linetype1.setFont(font)
        self.comboBox_linetype1.setObjectName("comboBox_linetype1")
        self.comboBox_linetype1.addItem("")
        self.comboBox_linetype1.addItem("")
        self.comboBox_linetype1.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_linetype1, 0, 2, 1, 1)
        self.pushButton_color2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_color2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_color2.setFont(font)
        self.pushButton_color2.setText("")
        self.pushButton_color2.setObjectName("pushButton_color2")
        self.gridLayout_2.addWidget(self.pushButton_color2, 1, 0, 1, 1)
        self.spinBox_thickness2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thickness2.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_thickness2.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_thickness2.setFont(font)
        self.spinBox_thickness2.setProperty("value", 2)
        self.spinBox_thickness2.setObjectName("spinBox_thickness2")
        self.gridLayout_2.addWidget(self.spinBox_thickness2, 1, 1, 1, 1)
        self.comboBox_linetype2 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_linetype2.setFont(font)
        self.comboBox_linetype2.setObjectName("comboBox_linetype2")
        self.comboBox_linetype2.addItem("")
        self.comboBox_linetype2.addItem("")
        self.comboBox_linetype2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_linetype2, 1, 2, 1, 1)
        self.pushButton_color3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_color3.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_color3.setFont(font)
        self.pushButton_color3.setText("")
        self.pushButton_color3.setObjectName("pushButton_color3")
        self.gridLayout_2.addWidget(self.pushButton_color3, 2, 0, 1, 1)
        self.spinBox_thickness3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thickness3.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_thickness3.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_thickness3.setFont(font)
        self.spinBox_thickness3.setProperty("value", 2)
        self.spinBox_thickness3.setObjectName("spinBox_thickness3")
        self.gridLayout_2.addWidget(self.spinBox_thickness3, 2, 1, 1, 1)
        self.comboBox_linetype3 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_linetype3.setFont(font)
        self.comboBox_linetype3.setObjectName("comboBox_linetype3")
        self.comboBox_linetype3.addItem("")
        self.comboBox_linetype3.addItem("")
        self.comboBox_linetype3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_linetype3, 2, 2, 1, 1)
        self.pushButton_color4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_color4.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_color4.setFont(font)
        self.pushButton_color4.setText("")
        self.pushButton_color4.setObjectName("pushButton_color4")
        self.gridLayout_2.addWidget(self.pushButton_color4, 3, 0, 1, 1)
        self.spinBox_thickness4 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thickness4.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_thickness4.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_thickness4.setFont(font)
        self.spinBox_thickness4.setProperty("value", 2)
        self.spinBox_thickness4.setObjectName("spinBox_thickness4")
        self.gridLayout_2.addWidget(self.spinBox_thickness4, 3, 1, 1, 1)
        self.comboBox_linetype4 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_linetype4.setFont(font)
        self.comboBox_linetype4.setObjectName("comboBox_linetype4")
        self.comboBox_linetype4.addItem("")
        self.comboBox_linetype4.addItem("")
        self.comboBox_linetype4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_linetype4, 3, 2, 1, 1)
        self.pushButton_color5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_color5.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_color5.setFont(font)
        self.pushButton_color5.setText("")
        self.pushButton_color5.setObjectName("pushButton_color5")
        self.gridLayout_2.addWidget(self.pushButton_color5, 4, 0, 1, 1)
        self.spinBox_thickness5 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thickness5.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_thickness5.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_thickness5.setFont(font)
        self.spinBox_thickness5.setProperty("value", 2)
        self.spinBox_thickness5.setObjectName("spinBox_thickness5")
        self.gridLayout_2.addWidget(self.spinBox_thickness5, 4, 1, 1, 1)
        self.comboBox_linetype5 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_linetype5.setFont(font)
        self.comboBox_linetype5.setObjectName("comboBox_linetype5")
        self.comboBox_linetype5.addItem("")
        self.comboBox_linetype5.addItem("")
        self.comboBox_linetype5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_linetype5, 4, 2, 1, 1)
        self.pushButton_color6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_color6.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_color6.setFont(font)
        self.pushButton_color6.setText("")
        self.pushButton_color6.setObjectName("pushButton_color6")
        self.gridLayout_2.addWidget(self.pushButton_color6, 5, 0, 1, 1)
        self.spinBox_thickness6 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thickness6.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_thickness6.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_thickness6.setFont(font)
        self.spinBox_thickness6.setProperty("value", 2)
        self.spinBox_thickness6.setObjectName("spinBox_thickness6")
        self.gridLayout_2.addWidget(self.spinBox_thickness6, 5, 1, 1, 1)
        self.comboBox_linetype6 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_linetype6.setFont(font)
        self.comboBox_linetype6.setObjectName("comboBox_linetype6")
        self.comboBox_linetype6.addItem("")
        self.comboBox_linetype6.addItem("")
        self.comboBox_linetype6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_linetype6, 5, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(40, 40, 244, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 360, 670, 72))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_S11 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_S11.setFont(font)
        self.pushButton_S11.setObjectName("pushButton_S11")
        self.horizontalLayout.addWidget(self.pushButton_S11)
        self.pushButton_S12 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_S12.setFont(font)
        self.pushButton_S12.setObjectName("pushButton_S12")
        self.horizontalLayout.addWidget(self.pushButton_S12)
        self.pushButton_S21 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_S21.setFont(font)
        self.pushButton_S21.setObjectName("pushButton_S21")
        self.horizontalLayout.addWidget(self.pushButton_S21)
        self.pushButton_S22 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_S22.setFont(font)
        self.pushButton_S22.setObjectName("pushButton_S22")
        self.horizontalLayout.addWidget(self.pushButton_S22)
        self.pushButton_VSWR1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_VSWR1.setFont(font)
        self.pushButton_VSWR1.setObjectName("pushButton_VSWR1")
        self.horizontalLayout.addWidget(self.pushButton_VSWR1)
        self.pushButton_VSWR2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_VSWR2.setFont(font)
        self.pushButton_VSWR2.setObjectName("pushButton_VSWR2")
        self.horizontalLayout.addWidget(self.pushButton_VSWR2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_Rx1_re = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Rx1_re.setFont(font)
        self.pushButton_Rx1_re.setObjectName("pushButton_Rx1_re")
        self.verticalLayout_2.addWidget(self.pushButton_Rx1_re)
        self.pushButton_Rx1_im = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Rx1_im.setObjectName("pushButton_Rx1_im")
        self.verticalLayout_2.addWidget(self.pushButton_Rx1_im)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_Rx2_re = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Rx2_re.setObjectName("pushButton_Rx2_re")
        self.verticalLayout_3.addWidget(self.pushButton_Rx2_re)
        self.pushButton_Rx2_im = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Rx2_im.setObjectName("pushButton_Rx2_im")
        self.verticalLayout_3.addWidget(self.pushButton_Rx2_im)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 9, 599, 237))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_open_file2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_open_file2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_open_file2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/nenuzhny/Pictures/FileIcon20x20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open_file2.setIcon(icon)
        self.pushButton_open_file2.setObjectName("pushButton_open_file2")
        self.gridLayout.addWidget(self.pushButton_open_file2, 2, 0, 1, 1)
        self.textEdit_fileName2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_fileName2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_fileName2.setObjectName("textEdit_fileName2")
        self.gridLayout.addWidget(self.textEdit_fileName2, 2, 1, 1, 6)
        self.textEdit_fileName1 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_fileName1.setMinimumSize(QtCore.QSize(500, 0))
        self.textEdit_fileName1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_fileName1.setObjectName("textEdit_fileName1")
        self.gridLayout.addWidget(self.textEdit_fileName1, 1, 1, 1, 6)
        self.checkBox_filePlot1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_filePlot1.setMaximumSize(QtCore.QSize(30, 30))
        self.checkBox_filePlot1.setText("")
        self.checkBox_filePlot1.setChecked(True)
        self.checkBox_filePlot1.setTristate(False)
        self.checkBox_filePlot1.setObjectName("checkBox_filePlot1")
        self.gridLayout.addWidget(self.checkBox_filePlot1, 1, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)
        self.pushButton_open_file1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_open_file1.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_open_file1.setText("")
        self.pushButton_open_file1.setIcon(icon)
        self.pushButton_open_file1.setObjectName("pushButton_open_file1")
        self.gridLayout.addWidget(self.pushButton_open_file1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.checkBox_filePlot2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_filePlot2.setMaximumSize(QtCore.QSize(30, 30))
        self.checkBox_filePlot2.setText("")
        self.checkBox_filePlot2.setChecked(True)
        self.checkBox_filePlot2.setObjectName("checkBox_filePlot2")
        self.gridLayout.addWidget(self.checkBox_filePlot2, 2, 7, 1, 1)
        self.pushButton_open_file3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_open_file3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_open_file3.setText("")
        self.pushButton_open_file3.setIcon(icon)
        self.pushButton_open_file3.setObjectName("pushButton_open_file3")
        self.gridLayout.addWidget(self.pushButton_open_file3, 3, 0, 1, 1)
        self.textEdit_fileName3 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_fileName3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_fileName3.setObjectName("textEdit_fileName3")
        self.gridLayout.addWidget(self.textEdit_fileName3, 3, 1, 1, 6)
        self.checkBox_filePlot3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_filePlot3.setMaximumSize(QtCore.QSize(30, 30))
        self.checkBox_filePlot3.setText("")
        self.checkBox_filePlot3.setChecked(True)
        self.checkBox_filePlot3.setObjectName("checkBox_filePlot3")
        self.gridLayout.addWidget(self.checkBox_filePlot3, 3, 7, 1, 1)
        self.pushButton_open_file4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_open_file4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_open_file4.setText("")
        self.pushButton_open_file4.setIcon(icon)
        self.pushButton_open_file4.setObjectName("pushButton_open_file4")
        self.gridLayout.addWidget(self.pushButton_open_file4, 4, 0, 1, 1)
        self.textEdit_fileName4 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_fileName4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_fileName4.setObjectName("textEdit_fileName4")
        self.gridLayout.addWidget(self.textEdit_fileName4, 4, 1, 1, 6)
        self.checkBox_filePlot4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_filePlot4.setMaximumSize(QtCore.QSize(30, 30))
        self.checkBox_filePlot4.setText("")
        self.checkBox_filePlot4.setChecked(True)
        self.checkBox_filePlot4.setObjectName("checkBox_filePlot4")
        self.gridLayout.addWidget(self.checkBox_filePlot4, 4, 7, 1, 1)
        self.pushButton_open_file5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_open_file5.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_open_file5.setText("")
        self.pushButton_open_file5.setIcon(icon)
        self.pushButton_open_file5.setObjectName("pushButton_open_file5")
        self.gridLayout.addWidget(self.pushButton_open_file5, 5, 0, 1, 1)
        self.textEdit_fileName5 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_fileName5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_fileName5.setObjectName("textEdit_fileName5")
        self.gridLayout.addWidget(self.textEdit_fileName5, 5, 1, 1, 6)
        self.checkBox_filePlot5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_filePlot5.setMaximumSize(QtCore.QSize(30, 30))
        self.checkBox_filePlot5.setText("")
        self.checkBox_filePlot5.setChecked(True)
        self.checkBox_filePlot5.setObjectName("checkBox_filePlot5")
        self.gridLayout.addWidget(self.checkBox_filePlot5, 5, 7, 1, 1)
        self.pushButton_open_file6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_open_file6.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_open_file6.setText("")
        self.pushButton_open_file6.setIcon(icon)
        self.pushButton_open_file6.setObjectName("pushButton_open_file6")
        self.gridLayout.addWidget(self.pushButton_open_file6, 6, 0, 1, 1)
        self.textEdit_fileName6 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_fileName6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_fileName6.setObjectName("textEdit_fileName6")
        self.gridLayout.addWidget(self.textEdit_fileName6, 6, 1, 1, 6)
        self.checkBox_filePlot6 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_filePlot6.setMaximumSize(QtCore.QSize(30, 30))
        self.checkBox_filePlot6.setText("")
        self.checkBox_filePlot6.setChecked(True)
        self.checkBox_filePlot6.setObjectName("checkBox_filePlot6")
        self.gridLayout.addWidget(self.checkBox_filePlot6, 6, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "Сопротивление"))
        self.comboBox_linetype1.setItemText(0, _translate("Dialog", "сплошная"))
        self.comboBox_linetype1.setItemText(1, _translate("Dialog", "штриховая"))
        self.comboBox_linetype1.setItemText(2, _translate("Dialog", "штрихпунктирная"))
        self.comboBox_linetype2.setItemText(0, _translate("Dialog", "сплошная"))
        self.comboBox_linetype2.setItemText(1, _translate("Dialog", "штриховая"))
        self.comboBox_linetype2.setItemText(2, _translate("Dialog", "штрихпунктирная"))
        self.comboBox_linetype3.setItemText(0, _translate("Dialog", "сплошная"))
        self.comboBox_linetype3.setItemText(1, _translate("Dialog", "штриховая"))
        self.comboBox_linetype3.setItemText(2, _translate("Dialog", "штрихпунктирная"))
        self.comboBox_linetype4.setItemText(0, _translate("Dialog", "сплошная"))
        self.comboBox_linetype4.setItemText(1, _translate("Dialog", "штриховая"))
        self.comboBox_linetype4.setItemText(2, _translate("Dialog", "штрихпунктирная"))
        self.comboBox_linetype5.setItemText(0, _translate("Dialog", "сплошная"))
        self.comboBox_linetype5.setItemText(1, _translate("Dialog", "штриховая"))
        self.comboBox_linetype5.setItemText(2, _translate("Dialog", "штрихпунктирная"))
        self.comboBox_linetype6.setItemText(0, _translate("Dialog", "сплошная"))
        self.comboBox_linetype6.setItemText(1, _translate("Dialog", "штриховая"))
        self.comboBox_linetype6.setItemText(2, _translate("Dialog", "штрихпунктирная"))
        self.label_4.setText(_translate("Dialog", "Цвет"))
        self.label_5.setText(_translate("Dialog", "Толщина"))
        self.label_6.setText(_translate("Dialog", "Тип линии"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Настройки"))
        self.pushButton_S11.setText(_translate("Dialog", "S11"))
        self.pushButton_S12.setText(_translate("Dialog", "S12"))
        self.pushButton_S21.setText(_translate("Dialog", "S21"))
        self.pushButton_S22.setText(_translate("Dialog", "S22"))
        self.pushButton_VSWR1.setText(_translate("Dialog", "VSWR1"))
        self.pushButton_VSWR2.setText(_translate("Dialog", "VSWR2"))
        self.pushButton_Rx1_re.setText(_translate("Dialog", "Rx1_re"))
        self.pushButton_Rx1_im.setText(_translate("Dialog", "Rx1_im"))
        self.pushButton_Rx2_re.setText(_translate("Dialog", "Rx2_re"))
        self.pushButton_Rx2_im.setText(_translate("Dialog", "Rx2_im"))
        self.label_3.setText(_translate("Dialog", "Вывод"))
        self.label.setText(_translate("Dialog", "Откр."))
        self.label_2.setText(_translate("Dialog", "Расположение файла"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Графики"))

