from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class BenchOperationsTable:
    def __init__(self, objlist):
        self.table = objlist['table']
        self.addBtn = objlist['addbtn']
        self.delBtn = objlist['delbtn']

        self.addBtn.clicked.connect(lambda: self.AddMaterial())
        self.delBtn.clicked.connect(lambda: self.DelMaterial())

        self.table.setRowCount(1)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("операция"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("мощность"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("кол-во часов"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("стоимость"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("кол-во"))

    def AddMaterial(self):
        print("AddBenchOperation")
        self.table.insertRow(1)

    def DelMaterial(self):
        print("DelBenchOperation")
        self.table.removeRow(1)
