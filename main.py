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
        self.ui.stackedWidget.setCurrentIndex(0)

        # Connect the push buttons to enable moving through pages
        self.ui.pushButton_6.clicked.connect(self.show_rec_payment)
        self.ui.pushButton_7.clicked.connect(self.show_transactions)
        self.ui.pushButton_8.clicked.connect(self.show_student_account)
        self.ui.pushButton_3.clicked.connect(self.show_add_student)
        self.ui.pushButton_9.clicked.connect(self.show_dash_board)

    def show_rec_payment(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_transactions(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_student_account(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_add_student(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_dash_board(self):
        self.ui.stackedWidget.setCurrentIndex(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
