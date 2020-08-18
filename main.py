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
        self.outputBox.setText("Sorry, that's not implemented yet!")

if __name__ == '__main__':
    app = QApplication([])
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
