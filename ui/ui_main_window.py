# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 419)
        MainWindow.setStyleSheet("#menu_widget, #toolBox {\n"
"    background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.menu_widget = QtWidgets.QWidget(self.splitter)
        self.menu_widget.setMinimumSize(QtCore.QSize(150, 0))
        self.menu_widget.setStyleSheet("background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.menu_widget.setObjectName("menu_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_widget)
        self.gridLayout.setContentsMargins(4, 4, 4, 15)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("#toolBox {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"    padding-left:5px;\n"
"    text-align:left;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"    background-color: #2d9cdb;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"    padding:5px 0px 5px 20px;\n"
"    text-align:left;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"    background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"    background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.students_page = QtWidgets.QWidget()
        self.students_page.setGeometry(QtCore.QRect(0, 0, 142, 298))
        self.students_page.setObjectName("students_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.students_page)
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.students_page)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.students_page)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.students_page)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.students_page)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48 (2).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.students_page, icon, "")
        self.educators_page = QtWidgets.QWidget()
        self.educators_page.setGeometry(QtCore.QRect(0, 0, 142, 298))
        self.educators_page.setObjectName("educators_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.educators_page)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.educators_page)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_14 = QtWidgets.QPushButton(self.educators_page)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_12 = QtWidgets.QPushButton(self.educators_page)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_4 = QtWidgets.QPushButton(self.educators_page)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/car-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.educators_page, icon1, "")
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setGeometry(QtCore.QRect(0, 0, 142, 298))
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.settings_page)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 388, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.settings_page, icon2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.all_transactions_page = QtWidgets.QWidget()
        self.all_transactions_page.setObjectName("all_transactions_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.all_transactions_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.all_transactions_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.all_transactions_page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.all_transactions_page)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.all_transactions_page)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.pushButton_13 = QtWidgets.QPushButton(self.all_transactions_page)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.all_transactions_page)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.all_transactions_page)
        self.addstudent_page = QtWidgets.QWidget()
        self.addstudent_page.setObjectName("addstudent_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.addstudent_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_24 = QtWidgets.QLabel(self.addstudent_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_22 = QtWidgets.QLabel(self.addstudent_page)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_7.addWidget(self.label_22)
        self.label_20 = QtWidgets.QLabel(self.addstudent_page)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.addstudent_page)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.label_23 = QtWidgets.QLabel(self.addstudent_page)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_7.addWidget(self.label_23)
        self.label_19 = QtWidgets.QLabel(self.addstudent_page)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.label_17 = QtWidgets.QLabel(self.addstudent_page)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.addstudent_page)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.addstudent_page)
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_6.addWidget(self.lineEdit_19)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.addstudent_page)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_6.addWidget(self.lineEdit_18)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.addstudent_page)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_6.addWidget(self.dateEdit_2)
        self.comboBox_4 = QtWidgets.QComboBox(self.addstudent_page)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_6.addWidget(self.comboBox_4)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.addstudent_page)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_6.addWidget(self.lineEdit_17)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.addstudent_page)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_6.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.addstudent_page)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_6.addWidget(self.lineEdit_16)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.pushButton_18 = QtWidgets.QPushButton(self.addstudent_page)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_11.addWidget(self.pushButton_18)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.addstudent_page)
        self.student_info_page = QtWidgets.QWidget()
        self.student_info_page.setObjectName("student_info_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.student_info_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.student_info_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.student_info_page)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.financial_details_tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.financial_details_tableWidget_2.sizePolicy().hasHeightForWidth())
        self.financial_details_tableWidget_2.setSizePolicy(sizePolicy)
        self.financial_details_tableWidget_2.setStyleSheet("")
        self.financial_details_tableWidget_2.setObjectName("financial_details_tableWidget_2")
        self.financial_details_tableWidget_2.setColumnCount(5)
        self.financial_details_tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.financial_details_tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.financial_details_tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.financial_details_tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.financial_details_tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.financial_details_tableWidget_2.setHorizontalHeaderItem(4, item)
        self.verticalLayout_9.addWidget(self.financial_details_tableWidget_2)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout_5.addWidget(self.tabWidget_2)
        self.stackedWidget.addWidget(self.student_info_page)
        self.receive_payment_page = QtWidgets.QWidget()
        self.receive_payment_page.setObjectName("receive_payment_page")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.receive_payment_page)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QtWidgets.QLabel(self.receive_payment_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_14.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.receive_payment_page)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.receive_payment_page)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.receive_payment_page)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_12.addWidget(self.label_16)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.receive_payment_page)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_11.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.receive_payment_page)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_11.addWidget(self.lineEdit_13)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.receive_payment_page)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_11.addWidget(self.lineEdit_14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.pushButton_17 = QtWidgets.QPushButton(self.receive_payment_page)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_5.addWidget(self.pushButton_17)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_14.addLayout(self.horizontalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 241, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem11)
        self.stackedWidget.addWidget(self.receive_payment_page)
        self.all_students_page = QtWidgets.QWidget()
        self.all_students_page.setObjectName("all_students_page")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.all_students_page)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_6 = QtWidgets.QLabel(self.all_students_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_16.addWidget(self.label_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.all_students_page)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_8.addWidget(self.lineEdit_20)
        self.pushButton_19 = QtWidgets.QPushButton(self.all_students_page)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_8.addWidget(self.pushButton_19)
        self.verticalLayout_16.addLayout(self.horizontalLayout_8)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.all_students_page)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_16.addWidget(self.tableWidget_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.all_students_page)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_10 = QtWidgets.QPushButton(self.all_students_page)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_2 = QtWidgets.QPushButton(self.all_students_page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout_16.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.all_students_page)
        self.dashboard_page = QtWidgets.QWidget()
        self.dashboard_page.setObjectName("dashboard_page")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.dashboard_page)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_5 = QtWidgets.QLabel(self.dashboard_page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_15.addWidget(self.label_5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 365, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem13)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)
        self.stackedWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Green Haven Secondary School"))
        self.pushButton_6.setText(_translate("MainWindow", "Recieve Payment"))
        self.pushButton_7.setText(_translate("MainWindow", "Transactions"))
        self.pushButton_8.setText(_translate("MainWindow", "Student Accounts"))
        self.pushButton_9.setText(_translate("MainWindow", "Dash Board"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.students_page), _translate("MainWindow", "Students"))
        self.pushButton_5.setText(_translate("MainWindow", "Add Educator"))
        self.pushButton_14.setText(_translate("MainWindow", "Pay Educator"))
        self.pushButton_12.setText(_translate("MainWindow", "Transactions"))
        self.pushButton_4.setText(_translate("MainWindow", "Dashboard"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.educators_page), _translate("MainWindow", "Educators"))
        self.pushButton_11.setText(_translate("MainWindow", "Dashboard"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.settings_page), _translate("MainWindow", "Settings"))
        self.label_4.setText(_translate("MainWindow", "All Transactions"))
        self.label_2.setText(_translate("MainWindow", "Filter"))
        self.pushButton_13.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Transaction #"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Learners Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount Paid"))
        self.label_24.setText(_translate("MainWindow", "Add Student"))
        self.label_22.setText(_translate("MainWindow", "Surname"))
        self.label_20.setText(_translate("MainWindow", "Name"))
        self.label_21.setText(_translate("MainWindow", "Date of Birth"))
        self.label_23.setText(_translate("MainWindow", "Gender"))
        self.label_19.setText(_translate("MainWindow", "Parent\'s Cell:"))
        self.label_17.setText(_translate("MainWindow", "Address"))
        self.label_18.setText(_translate("MainWindow", "Email Address"))
        self.pushButton_18.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Student\'s Name"))
        item = self.financial_details_tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.financial_details_tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Transaction #"))
        item = self.financial_details_tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.financial_details_tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount Paid"))
        item = self.financial_details_tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount Owing"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Financial details"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Biographical Details"))
        self.label.setText(_translate("MainWindow", "Receive Payment"))
        self.label_14.setText(_translate("MainWindow", "Name"))
        self.label_15.setText(_translate("MainWindow", "Surname"))
        self.label_16.setText(_translate("MainWindow", "Amount"))
        self.pushButton_17.setText(_translate("MainWindow", "Pay"))
        self.label_6.setText(_translate("MainWindow", "Student Accounts"))
        self.pushButton_19.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_10.setText(_translate("MainWindow", "Edit"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.label_5.setText(_translate("MainWindow", "Dash Board"))
