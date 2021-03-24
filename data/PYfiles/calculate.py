from PyQt5.QtWidgets import QApplication, QWidget
from main import ManHourTableRes, BenchTableRes, OptMatRes, tax


class Calculator:
    def __init__(self, objlist):
        self.resultBtn = objlist['resbtn']
        self.ResultLCD = objlist['reslcd']
        self.Opttable = objlist['optmattable']
        self.Benchtable = objlist['benchtable']
        self.Manhtable = objlist['manhourtable']

        self.resultBtn.clicked.connect(lambda: self.Result())

    def Result(self):
        global ManHourTableRes, BenchTableRes, OptMatRes, tax

        try:
            OptMatResult = 0
            for i in range(self.Opttable.rowCount()):
                OptMatResult += float(self.Opttable.item(i, 1).text()) * float(self.Opttable.item(i, 2).text())
            OptMatRes = OptMatResult
        except BaseException as er:
            print(er)

        try:
            ManHourTableResult = 0
            for i in range(self.Manhtable.rowCount()):
                ManHourTableResult += float(self.Manhtable.item(i, 1).text()) * float(self.Manhtable.item(i, 2).text())
            ManHourTableRes = ManHourTableResult
        except BaseException as er:
            print(er)

        try:
            BenchTableResult = 0
            for i in range(self.Benchtable.rowCount()):
                BenchTableResult += float(self.Benchtable.item(i, 3).text()) * float(self.Benchtable.item(i, 4).text()) + \
                                 (float(self.Benchtable.item(i, 1).text()) * float(self.Benchtable.item(i, 2).text()) *
                                  tax)
            BenchTableRes = BenchTableResult
        except BaseException as er:
            print(er)

        result = ManHourTableRes + BenchTableRes + OptMatRes
        self.ResultLCD.display(result)
