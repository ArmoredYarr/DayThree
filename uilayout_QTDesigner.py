from PyQt5.QtWidgets import *
from PyQt5 import uic

logins = {
    'wumbo': 'wackadoo',
    'wonk': 'dootsmack'
}

class GUI(QMainWindow):
    # In order to use the design made in qtdesigner...
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('design.ui', self)
        self.show()

        self.loginButton.clicked.connect(self.login)

    def login(self):
        # Do not do this for real, especially do not show that a username exists and the password is wrong.
        # and never check a password or store it as plain text. There's all kinds of things wrong here.
        # This is just as an example.
        if self.lineEdit.text() == 'wumbo':
            if self.lineEdit_2.text() == logins['wumbo']:
                show_login_result('Logged in as wumbo')
            else:
                show_login_result("Incorrect password.")
        elif self.lineEdit.text() == 'wonk':
            if self.lineEdit_2.text() == logins['wonk']:
                show_login_result('Logged in as wonk')
            else:
                show_login_result("Incorrect password.")
        else:
            show_login_result("Username does not exist.")

def show_login_result(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

def main():
    app = QApplication([])
    window = GUI()
    app.exec_()


if __name__ == "__main__":
    main()