import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from PyQt5 import uic
from data.PYfiles.dopMat_table import *
from data.PYfiles.mh_table import *
from data.PYfiles.stan_ui import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/gui/itfestmainui.ui', self)  # выбор дизайна приложения
        self.setWindowTitle('CPO')  # выбор названия приложения


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())