# We're taking it all. All the widgets.
from PyQt5.QtWidgets import *
# I saw you there, QTWebSockets. I may be seeing you soon.
from PyQt5.QtGui import QFont

#For simplicity I will follow the example, however you should probably make each window of the application
# It's own class. Especially if it's a larger application, this will certainly help later on down the line.
def main_window():
    # To set up the application, you need at least a blank list for args.
    app = QApplication([])
    # This constructs a window. 
    window = QWidget()
    # You can construct multiple windows in the same fashion.
    #window2 = QWidget()

    #We can control the size and shape of the window like so.
    #The first two values are the X and Y of where to START drawing the window, the last two are the SIZE of it.
    window.setGeometry(100,100, 200, 200)

    #You can set the title of the window.
    window.setWindowTitle("Ohai.")

    # ========== Add stuff to the window here.=============
    # To add something to a window you create it and pass it the window you want it on.

    #A label is pretty simple. You can pass a string as the first arguement to set it's text or use the setText func.
    label = QLabel('Ahoy', window)

    #In order to change the font you need QFont like so.
    label.setFont(QFont("Arial", 22))

    # You can set all kinds of different styling in a similar syntax to CSS 
    # Here  I'll set the color to light green and give it a border, much like you would in CSS for an HTML document.
    label.setStyleSheet("color: lightgreen; \
                        border: 1px solid green;")

    #You can move widgets around manually like so.
    label.move(20, 30)

    # To show the window (You can hide and show them, useful for multi-window applications.)
    window.show()
    # If you have a second window, it works much the same way.
    #window2.show()

    #This will actually fire the QApplication and put everything together.
    app.exec_()

if __name__ == "__main__":
    print("It's time to GUI.")
    main_window()