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

        optionalMaterialList = {'table': self.mat_table, 'addbtn': self.mat_add, 'delbtn': self.mat_del}
        OptMat = OptionalMaterialsTable(optionalMaterialList)

        ManHoursList = {'table': self.mh_table, 'addbtn': self.mh_add, 'delbtn': self.mh_del}
        MHTable = ManHoursTable(ManHoursList)

        BenchList = {'table': self.bench_list_table, 'addbtn': self.bench_add, 'delbtn': self.bench_del}
        BenchTable = BenchOperationsTable(BenchList)
        print("STARTED")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
