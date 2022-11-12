import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QCompleter
from PyQt5 import QtCore, QtWidgets
from datetime import date
from ui.ui_main_window import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *
from message_boxes import show_info_messagebox_2


# delegates class to align text inside Qtablewidget
class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


# Initial setup of main window
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_completer()  # For search autocomplete

        # set the app to open first page on launch
        self.ui.stackedWidget.setCurrentIndex(4)
        self.get_data_students()

        # Connect the push buttons to enable page navigation
        self.ui.pushButton_6.clicked.connect(self.show_rec_payment)
        self.ui.pushButton_7.clicked.connect(self.show_transactions)
        self.ui.pushButton_8.clicked.connect(self.show_student_account)
        self.ui.pushButton_9.clicked.connect(self.show_dash_board)
        self.ui.pushButton_17.clicked.connect(self.add_transaction)
        self.ui.pushButton_7.clicked.connect(self.get_data)
        self.ui.pushButton_13.clicked.connect(self.transactions_search)
        self.ui.pushButton_18.clicked.connect(self.add_student)
        self.ui.pushButton.clicked.connect(self.show_add_student)
        self.ui.pushButton_8.clicked.connect(self.get_data_students)
        self.ui.pushButton_19.clicked.connect(self.students_search)

        # Transactions table
        # Stretch widget to fill whole page
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Using delegates to align text inside
        delegate = AlignDelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegateForColumn(1, delegate)
        self.ui.tableWidget.setItemDelegateForColumn(4, delegate)  # You can repeat this line or use a simple
        # iteration/to align multiple columns
        # If you want to do it for all columns:
        # self.tableWidget.setItemDelegate(delegate)

        # Students table
        # Stretch widget to fill whole page
        self.ui.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Using delegates to align text inside Transactions table
        delegate = AlignDelegate(self.ui.tableWidget_2)
        self.ui.tableWidget_2.setItemDelegateForColumn(0, delegate)
        self.ui.tableWidget_2.setItemDelegate(delegate)

    # Functions to enable page navigation
    def show_rec_payment(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_transactions(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_student_account(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def show_dash_board(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def show_add_student(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    # Functionality functions
    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def add_transaction(self):
        """ create a transaction and add it to transactions table in the database
                    specified by the db_file
                :param
                :return:
                """
        try:
            database = r"my_db.db"

            # create a database connection
            conn = self.create_connection(database)
            with conn:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                today = date.today()
                # dd/mm/YY
                d_string = today.strftime("%d/%m/%Y")

                row = (d_string, self.ui.lineEdit_12.text(), self.ui.lineEdit_13.text(), self.ui.doubleSpinBox.value())

                # Preparing SQL queries to INSERT a record into the database.
                command = '''INSERT INTO transactions(date, name, surname, amount) VALUES (?,?,?,?)'''
                cursor.execute(command, row)

                show_info_messagebox_2("The payment was added successfully")

                # Clear all the texts from line edits
                self.ui.lineEdit_12.clear()
                self.ui.lineEdit_13.clear()
                self.ui.doubleSpinBox.clear()

                self.init_completer()

                # Commit your changes in the database
                conn.commit()

                cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if conn:
                conn.close()

    def add_student(self):
        """ create a student object and add it to students table in the database
                           specified by the db_file
                       :param
                       :return:
                       """
        try:
            database = r"my_db.db"

            # create a database connection
            conn = self.create_connection(database)
            with conn:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                today = date.today()
                # dd/mm/YY
                d_string = today.strftime("%d/%m/%Y")

                row = (self.ui.lineEdit_18.text(), self.ui.lineEdit_19.text(), self.ui.dateEdit_2.text(),
                       self.ui.comboBox_4.currentText(), self.ui.lineEdit_17.text(), self.ui.lineEdit_15.text(),
                       self.ui.lineEdit_16.text(), d_string)

                # Preparing SQL queries to INSERT a record into the database.
                command = '''INSERT INTO students(name, surname, dob, gender, parents_cell, pysical_address, email_address, date_joined) VALUES (?,?,?,?,?,?,?,?)'''
                cursor.execute(command, row)

                show_info_messagebox_2("student was added successfully")
                self.ui.lineEdit_18.clear()
                self.ui.lineEdit_19.clear()
                self.ui.dateEdit_2.clear()
                self.ui.comboBox_4.clear()
                self.ui.lineEdit_17.clear()
                self.ui.lineEdit_15.clear()
                self.ui.lineEdit_16.clear()

                self.init_completer()

                # Commit your changes in the database
                conn.commit()

                cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if conn:
                conn.close()

                # Clear all the texts from line edits

    def get_data(self):
        """ fetch data from database table and display on QWidget
                        :param
                        :return:
                        """
        try:
            database = r"my_db.db"

            # create a database connection
            conn = self.create_connection(database)
            with conn:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                command = '''SELECT * from transactions'''

                result = cursor.execute(command)

                self.ui.tableWidget.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def get_data_students(self):
        """ fetch data from students table and display on QWidget
                        :param
                        :return:
                        """
        try:
            database = r"my_db.db"

            # create a database connection
            conn = self.create_connection(database)
            with conn:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                command = '''SELECT * from students'''

                result = cursor.execute(command)

                self.ui.tableWidget_2.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget_2.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def init_completer(self):
        """ enable autocomplete on search lineEdit
                :param
                :return:
                """
        database = r"my_db.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            cursor = conn.cursor()

            # For transactions search
            cursor.execute(" SELECT name FROM transactions ")
            results = cursor.fetchall()

            new_list = [i[0] for i in results]

            completer = QCompleter(new_list)
            self.ui.lineEdit_4.setCompleter(completer)

            # For students name search
            cursor.execute(" SELECT name FROM students ")
            results = cursor.fetchall()

            new_list = [i[0] for i in results]

            completer = QCompleter(new_list)
            self.ui.lineEdit_20.setCompleter(completer)
            self.ui.lineEdit_18.setCompleter(completer)
            self.ui.lineEdit_12.setCompleter(completer)

            # For students name search
            cursor.execute(" SELECT surname FROM students ")
            results = cursor.fetchall()

            new_list = [i[0] for i in results]

            completer = QCompleter(new_list)
            self.ui.lineEdit_19.setCompleter(completer)
            self.ui.lineEdit_13.setCompleter(completer)

    def transactions_search(self):
        try:
            database = r"my_db.db"

            # create a database connection
            conn = self.create_connection(database)
            with conn:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                nbr = self.ui.lineEdit_4.text()

                command = '''SELECT * from transactions WHERE name=?'''

                result = cursor.execute(command, [nbr])

                self.ui.tableWidget.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def students_search(self):
        try:
            database = r"my_db.db"

            # create a database connection
            conn = self.create_connection(database)
            with conn:
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                nbr = self.ui.lineEdit_20.text()

                command = '''SELECT * from students WHERE name=?'''

                result = cursor.execute(command, [nbr])

                self.ui.tableWidget_2.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget_2.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
