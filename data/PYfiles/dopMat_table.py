from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class OptionalMaterialsTable:
    def __init__(self, objlist):
        self.table = objlist['table']
        self.addBtn = objlist['addbtn']
        self.delBtn = objlist['delbtn']

        self.addBtn.clicked.connect(lambda: self.AddMaterial())
        self.delBtn.clicked.connect(lambda: self.DelMaterial())

        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("операция"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("стоимость"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("кол-во"))

    def AddMaterial(self):
        print("AddMaterial")
        self.table.insertRow(1)

    def DelMaterial(self):
        print("DelMaterial")
        self.table.removeRow(1)
