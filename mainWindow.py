from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(960, 540, 800, 600)
    window.setWindowTitle("Coba Qt manual di VSCode !")
    window.show()
    sys.exit(app.exec_())


window()
