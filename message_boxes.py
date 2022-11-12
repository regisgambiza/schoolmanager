from PyQt5.QtWidgets import *

# makes sound
def show_info_messagebox(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    # setting message for Message Box
    msg.setText(message)

    # setting Message box window title
    msg.setWindowTitle("Information MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    # start the app
    retval = msg.exec_()

# Does not make sound
def show_info_messagebox_2(message):
    msgBox = QMessageBox()
    msgBox.setText(message)
    msgBox.setInformativeText("Click OK to continue!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    # msgBox.setDefaultButton(QMessageBox.Save)
    ret = msgBox.exec()


def show_warning_messagebox():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    # setting message for Message Box
    msg.setText("Warning")

    # setting Message box window title
    msg.setWindowTitle("Warning MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    # start the app
    retval = msg.exec_()


def show_question_messagebox():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)

    # setting message for Message Box
    msg.setText("Question")

    # setting Message box window title
    msg.setWindowTitle("Question MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    # start the app
    retval = msg.exec_()


def show_critical_messagebox():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    # setting message for Message Box
    msg.setText("Critical")

    # setting Message box window title
    msg.setWindowTitle("Critical MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    # start the app
    retval = msg.exec_()