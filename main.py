import sqlite3
from sqlite3 import Error

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.ui_main_window import Ui_MainWindow
import sys


# Initial setup of main window
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set the app to open first page on launch
        self.ui.stackedWidget.setCurrentIndex(4)

        # Connect the push buttons to enable page navigation
        self.ui.pushButton_6.clicked.connect(self.show_rec_payment)
        self.ui.pushButton_7.clicked.connect(self.show_transactions)
        self.ui.pushButton_8.clicked.connect(self.show_student_account)
        self.ui.pushButton_9.clicked.connect(self.show_dash_board)

    # Functions to enable page navigation
    def show_rec_payment(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_transactions(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_student_account(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def show_dash_board(self):
        self.ui.stackedWidget.setCurrentIndex(5)


# The following functions are for connecting and getting info from the database
def create_connection(db_file):
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


def select_all_students(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"my_db.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Query all students")
        select_all_students(conn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
