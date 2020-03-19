from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from PyQt5.QtGui import QColor
import sys
from design import Ui_Form as Design
import csv


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.schools = {}
        with open('rez.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                a = '","'
                if str(row[0].split(a)[0].split('"')[1].split()[1]) not in self.schools:
                    self.schools[str(row[0].split(a)[0].split('"')[1].split()[1])] = {}
                if str(row[0].split(a)[0].split('"')[1].split()[2]) not in self.schools[
                    str(row[0].split(a)[0].split('"')[1].split()[1])]:
                    self.schools[str(row[0].split(a)[0].split('"')[1].split()[1])][
                        str(row[0].split(a)[0].split('"')[1].split()[2])] = [row]
                else:
                    self.schools[str(row[0].split(a)[0].split('"')[1].split()[1])][
                        str(row[0].split(a)[0].split('"')[1].split()[2])].append(row)
        m = []
        d = []
        for i in sorted(self.schools):
            if i not in m:
                self.comboBox.addItem(i)
                m.append(i)
            for j in sorted(self.schools[i]):
                if j not in d:
                    self.comboBox_2.addItem(j)
                    d.append(j)
        self.pushButton.clicked.connect(self.click)
        self.click()

    def click(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        count = 0
        scores = []
        if self.comboBox.currentText() == 'Школа' and self.comboBox_2.currentText() == 'Класс':
            for i in self.schools:
                for j in self.schools[i]:
                    for k in self.schools[i][j]:
                        count += 1
                        self.tableWidget.setRowCount(count)
                        self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0].split('","')[1]))
                        self.tableWidget.setItem(count - 1, 1,
                                                 QTableWidgetItem(' '.join(k[0].split('","')[0].split()[-2:])))
                        self.tableWidget.setItem(count - 1, 2, QTableWidgetItem(k[0].split('","')[-1][:-1]))
                        scores.append([int(k[0].split('","')[-1][:-1]), count - 1])
        elif self.comboBox.currentText() == 'Школа':
            for i in self.schools:
                for j in self.schools[i]:
                    if j == self.comboBox_2.currentText():
                        for k in self.schools[i][j]:
                            count += 1
                            self.tableWidget.setRowCount(count)
                            self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0]))
                            self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0].split('","')[1]))
                            self.tableWidget.setItem(count - 1, 1,
                                                     QTableWidgetItem(' '.join(k[0].split('","')[0].split()[-2:])))
                            self.tableWidget.setItem(count - 1, 2, QTableWidgetItem(k[0].split('","')[-1][:-1]))
                            scores.append([int(k[0].split('","')[-1][:-1]), count - 1])
        elif self.comboBox_2.currentText() == 'Класс':
            for i in self.schools:
                if i == self.comboBox.currentText():
                    for j in self.schools[i]:
                        for k in self.schools[i][j]:
                            count += 1
                            self.tableWidget.setRowCount(count)
                            self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0]))
                            self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0].split('","')[1]))
                            self.tableWidget.setItem(count - 1, 1,
                                                     QTableWidgetItem(' '.join(k[0].split('","')[0].split()[-2:])))
                            self.tableWidget.setItem(count - 1, 2, QTableWidgetItem(k[0].split('","')[-1][:-1]))
                            scores.append([int(k[0].split('","')[-1][:-1]), count - 1])
        else:
            for i in self.schools:
                if i == self.comboBox.currentText():
                    for j in self.schools[i]:
                        if j == self.comboBox_2.currentText():
                            for k in self.schools[i][j]:
                                count += 1
                                self.tableWidget.setRowCount(count)
                                self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0]))
                                self.tableWidget.setItem(count - 1, 0, QTableWidgetItem(k[0].split('","')[1]))
                                self.tableWidget.setItem(count - 1, 1,
                                                         QTableWidgetItem(' '.join(k[0].split('","')[0].split()[-2:])))
                                self.tableWidget.setItem(count - 1, 2, QTableWidgetItem(k[0].split('","')[-1][:-1]))
                                scores.append([int(k[0].split('","')[-1][:-1]), count - 1])
        if len(scores) <= 3:
            for i in list(sorted(scores, reverse=True)):
                self.tableWidget.item(i[-1], 2).setForeground(QColor("red"))
        else:
            for i in range(3):
                self.tableWidget.item(list(sorted(scores, reverse=True))[i][-1], 2).setForeground(QColor("red"))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())