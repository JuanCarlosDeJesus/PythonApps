# GUI Text Editor using PyQT6
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()

        self.setWindowTitle("Generic Notepad Clone")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

    def change_size(self, size):
        self.textEdit.setFont(QFont("Arial", size))


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()
