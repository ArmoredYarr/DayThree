from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def button_clicked(msg):
    # This will create a popup message with the text [msg].
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

def main_window():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100, 200, 200)
    window.setWindowTitle("Ohai.")

    # ========== Add stuff to the window here.=============
    layout = QVBoxLayout() #Vertical Box layout.
    label = QLabel('Press Butan.')

    text_box = QTextEdit()

    button = QPushButton('DO IT')
    #To link a button to a function:
    #Use a lambda so the function doesn't run unless the event is triggered.
    button.clicked.connect(lambda: button_clicked(text_box.toPlainText()))

    #Then to add the qidgets to the layout...
    layout.addWidget(label)
    layout.addWidget(text_box)
    layout.addWidget(button)

    window.setLayout(layout)


    window.show()

    app.exec_()

if __name__ == "__main__":
    print("It's time to GUI.")
    main_window()