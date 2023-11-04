import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from statistics import mean
import math


def fixed_num(n, prec=0):
   return f"{n:.{prec}f}"


class MainWindow(QMainWindow):
   def __init__(self):
       QMainWindow.__init__(self)

       self.setMinimumSize(QSize(1000, 1000))  # Set sizes
       self.setWindowTitle("Дополнительное задание к лабораторной №0")  # Set the window title
       central_widget = QWidget(self)  # Create a central widget
       self.setCentralWidget(central_widget)  # Install the central widget

       self.grid_layout = QGridLayout(self)  # Create QGridLayout
       central_widget.setLayout(self.grid_layout)  # Set this layout in central widget

       self.table = QTableWidget(self)  # Create a table
       self.table.setColumnCount(5)  # Set three columns
       self.table.setRowCount(20)  # and one row

       # Set the table headers
       self.table.setHorizontalHeaderLabels(["△Di, мм", "△Di, мм", "△Di2, мм2", "△Di, мм", "△Di2, мм2"])

       # Установка значений по умолчанию
       default_values = ["10.47", "10.45", "10.47", "10.46", "10.49",
                         "10.46", "10.48", "10.46", "10.46", "10.48",
                         "10.46", "10.49", "10.47", "10.46", "10.47",
                         "10.46", "10.48", "10.45", "10.46", "10.48"]
       for row, value in enumerate(default_values):
           self.table.setItem(row, 0, self.createTableItem(value))

       # 10.47 10.45 10.47 10.46 10.49 10.46 10.48 10.46 10.46 10.48 10.46 10.49 10.47 10.46 10.47 10.46 10.48 10.45 10.46 10.48
       list = [10.47, 10.45, 10.47, 10.46, 10.49, 10.46, 10.48, 10.46, 10.46, 10.48, 10.46, 10.49, 10.47, 10.46, 10.47, 10.46, 10.48, 10.45, 10.46, 10.48]
       D20 = round(mean(list), 3)
       D5 = round(mean(list[:5]), 3)
       list_otklon_5 = [round(i - D5, 3) for i in list[:5]]
       list_otklon_20 = [round(i - D20, 3) for i in list]

       for i in range(20):
           self.table.setItem(i, 2, QTableWidgetItem(fixed_num(pow(list_otklon_20[i], 2), 6)))
       for i in range(5):
           self.table.setItem(i, 4, QTableWidgetItem(fixed_num(pow(list_otklon_5[i], 2), 6)))

       for i in range(20):
           self.table.setItem(i, 1, QTableWidgetItem(str(list_otklon_20[i])))
       for i in range(5):
           self.table.setItem(i, 3, QTableWidgetItem(str(list_otklon_5[i])))

       sum_5 = sum([int((i ** 2) * (10 ** 6)) for i in list_otklon_5])
       sum_20 = sum([int((i ** 2) * (10 ** 6)) for i in list_otklon_20])

       sn_5 = fixed_num(math.sqrt(sum_5 / 4) * 10 ** (-3), 6)
       sn_20 = fixed_num(math.sqrt(sum_20 / 19) * 10 ** (-3), 6)

       sn_5_ = fixed_num(math.sqrt(sum_5 / (5 * 4)) * 10 ** (-3), 6)
       sn_20_ = fixed_num(math.sqrt(sum_20 / (20 * 19)) * 10 ** (-3), 6)

       list_otklon_5_abs = [abs(i) for i in list_otklon_5]
       list_otklon_20_abs = [abs(i) for i in list_otklon_20]

       delta_D5 = round(mean(list_otklon_5_abs), 5)
       delta_D20 = round(mean(list_otklon_20_abs), 5)
       # Do the resize of the columns by content
       self.table.resizeColumnsToContents()

       self.grid_layout.addWidget(self.table, 0, 0)  # Adding the table to the grid

       pybutton = QPushButton('Показать результат', self)  # Create a button
       pybutton.clicked.connect(self.clickMethod)
       pybutton.resize(270, 100)
       pybutton.move(588, 700)

       # creating a label widget
       self.label = QLabel(f"<D5> = {D20}\n<△D5> = {delta_D5}\nS5 = {sn_5}\nS’5 = {sn_5_}\n"
                           f"\n<D20> = {D5}\n<△D20> = {delta_D20}\nS20 = {sn_20}\nS’20 = {sn_20_}", self)
       # moving position
       self.label.move(600, 300)
       # setting up border
       self.label.setFont(QFont('Arial', 10))
       self.label.setAlignment(Qt.AlignCenter)
       self.label.resize(270, 300)
       self.label.setStyleSheet("background-color: white;"
                                "border: 1px solid black;")
       self.label.hide()

       pybutton_2 = QPushButton('Ввести свои данные', self)  # Create a button
       pybutton_2.clicked.connect(self.clickMethod_2)
       pybutton_2.resize(270, 100)
       pybutton_2.move(588, 850)

       self.input = QLineEdit("Введите измерения через пробел (Вместо этого текста)", self)
       self.input.resize(436, 50)
       self.input.move(548, 800)

   def createTableItem(self, value):
       # Создание ячейки таблицы
       item = QTableWidgetItem()
       item.setText(value)
       return item

   def clickMethod(self):
       list = [0 for i in range(20)]
       for row in range(20):
           item = self.table.item(row, 0)
           list[row] = float(item.text())
       print(list)
       for i in range(20):
           self.table.setItem(i, 0, QTableWidgetItem(str(list[i])))
       print(list)
       D20 = round(mean(list), 3)
       D5 = round(mean(list[:5]), 3)
       list_otklon_5 = [round(i - D5, 3) for i in list[:5]]
       list_otklon_20 = [round(i - D20, 3) for i in list]

       for i in range(20):
           self.table.setItem(i, 2, QTableWidgetItem(fixed_num(pow(list_otklon_20[i], 2), 6)))
       for i in range(5):
           self.table.setItem(i, 4, QTableWidgetItem(fixed_num(pow(list_otklon_5[i], 2), 6)))

       for i in range(20):
           self.table.setItem(i, 1, QTableWidgetItem(str(list_otklon_20[i])))
       for i in range(5):
           self.table.setItem(i, 3, QTableWidgetItem(str(list_otklon_5[i])))
       print(list)
       sum_5 = sum([int((i ** 2) * (10 ** 6)) for i in list_otklon_5])
       sum_20 = sum([int((i ** 2) * (10 ** 6)) for i in list_otklon_20])

       sn_5 = fixed_num(math.sqrt(sum_5 / 4) * 10 ** (-3), 6)
       sn_20 = fixed_num(math.sqrt(sum_20 / 19) * 10 ** (-3), 6)

       sn_5_ = fixed_num(math.sqrt(sum_5 / (5 * 4)) * 10 ** (-3), 6)
       sn_20_ = fixed_num(math.sqrt(sum_20 / (20 * 19)) * 10 ** (-3), 6)

       list_otklon_5_abs = [abs(i) for i in list_otklon_5]
       list_otklon_20_abs = [abs(i) for i in list_otklon_20]

       delta_D5 = round(mean(list_otklon_5_abs), 5)
       delta_D20 = round(mean(list_otklon_20_abs), 5)
       # Do the resize of the columns by content
       self.table.resizeColumnsToContents()
       print(list)
       self.label = QLabel(f"<D5> = {D5}\n<△D5> = {delta_D5}\nS5 = {sn_5}\nS’5 = {sn_5_}\n"
                           f"\n<D20> = {D20}\n<△D20> = {delta_D20}\nS20 = {sn_20}\nS’20 = {sn_20_}", self)
       # moving position
       self.label.move(600, 300)
       # setting up border
       self.label.setFont(QFont('Arial', 10))
       self.label.setAlignment(Qt.AlignCenter)
       self.label.resize(270, 300)
       self.label.setStyleSheet("background-color: white;"
                                "border: 1px solid black;")

       self.grid_layout.addWidget(self.table, 0, 0)  # Adding the table to the grid
       self.label.show()

   def clickMethod_2(self):
       text = self.input.text()
       text = text.split()

       list = [0 for i in range(20)]
       for i in range(len(text)):
           list[i] = float(text[i])
       self.table = QTableWidget(self)  # Create a table
       self.table.setColumnCount(5)  # Set three columns
       self.table.setRowCount(20)  # and one row
       # Set the table headers
       self.table.setHorizontalHeaderLabels(["△Di, мм", "△Di, мм", "△Di2, мм2", "△Di, мм", "△Di2, мм2"])
       for i in range(20):
           self.table.setItem(i, 0, QTableWidgetItem(str(list[i])))

       D20 = round(mean(list), 3)
       D5 = round(mean(list[:5]), 3)
       list_otklon_5 = [round(i - D5, 3) for i in list[:5]]
       list_otklon_20 = [round(i - D20, 3) for i in list]

       for i in range(20):
           self.table.setItem(i, 2, QTableWidgetItem(fixed_num(pow(list_otklon_20[i], 2), 6)))
       for i in range(5):
           self.table.setItem(i, 4, QTableWidgetItem(fixed_num(pow(list_otklon_5[i], 2), 6)))

       for i in range(20):
           self.table.setItem(i, 1, QTableWidgetItem(str(list_otklon_20[i])))
       for i in range(5):
           self.table.setItem(i, 3, QTableWidgetItem(str(list_otklon_5[i])))

       sum_5 = sum([int((i ** 2) * (10 ** 6)) for i in list_otklon_5])
       sum_20 = sum([int((i ** 2) * (10 ** 6)) for i in list_otklon_20])

       sn_5 = fixed_num(math.sqrt(sum_5 / 4) * 10 ** (-3), 6)
       sn_20 = fixed_num(math.sqrt(sum_20 / 19) * 10 ** (-3), 6)

       sn_5_ = fixed_num(math.sqrt(sum_5 / (5 * 4)) * 10 ** (-3), 6)
       sn_20_ = fixed_num(math.sqrt(sum_20 / (20 * 19)) * 10 ** (-3), 6)

       list_otklon_5_abs = [abs(i) for i in list_otklon_5]
       list_otklon_20_abs = [abs(i) for i in list_otklon_20]

       delta_D5 = round(mean(list_otklon_5_abs), 5)
       delta_D20 = round(mean(list_otklon_20_abs), 5)
       # Do the resize of the columns by content
       self.table.resizeColumnsToContents()

       self.label = QLabel(f"<D5> = {D5}\n<△D5> = {delta_D5}\nS5 = {sn_5}\nS’5 = {sn_5_}\n"
                           f"\n<D20> = {D20}\n<△D20> = {delta_D20}\nS20 = {sn_20}\nS’20 = {sn_20_}", self)
       # moving position
       self.label.move(600, 300)
       # setting up border
       self.label.setFont(QFont('Arial', 10))
       self.label.setAlignment(Qt.AlignCenter)
       self.label.resize(270, 300)
       self.label.setStyleSheet("background-color: white;"
                                "border: 1px solid black;")

       self.grid_layout.addWidget(self.table, 0, 0)  # Adding the table to the grid


if __name__ == "__main__":
   app = QApplication(sys.argv)
   mw = MainWindow()
   mw.show()
   sys.exit(app.exec())
