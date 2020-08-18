import sys, PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 420, 660)
        self.inputBox = QTextEdit(self)
        self.inputBox.setGeometry(10, 10, 400, 300)
        self.inputBox.setText("Type here:")

        self.convertBtn = QPushButton(self)
        self.convertBtn.setGeometry(135, 320, 150, 20)
        self.convertBtn.setText("CoNvErT tO fUnKy CaPs")
        self.convertBtn.clicked.connect(self.convert)

        self.outputBox = QTextEdit(self)
        self.outputBox.setGeometry(10, 350, 400, 300)
        self.outputBox.setText("Output will be printed here.")

    def convert(self):
        upper = False
        strIn = self.inputBox.toPlainText()
        strOut = ''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ'
        for c in strIn:
            if c in chars:
                if upper:
                    strOut += c.upper()
                else:
                    strOut += c.lower()
                upper = not upper
            else:
                strOut += c
        self.outputBox.setText(strOut)

if __name__ == '__main__':
    app = QApplication([])
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
