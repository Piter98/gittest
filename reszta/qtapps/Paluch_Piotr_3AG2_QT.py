#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QSpinBox
from PyQt5.QtWidgets import QSlider, QLCDNumber

class Konwerter(QWidget):
    def __init__(self, parent=None):
        super(Konwerter, self).__init__(parent)

        self.interfejs()

    def interfejs(self):
        # etykiety
        etykieta0 = QLabel("Konwerter")
        etykieta01 = QLabel("Wybierz jednostkę:")
        etykieta1 = QLabel("Wartość")
        etykieta11 = QLabel("Jednostka docelowa:")
        etykieta2 = QLabel("Wybrana zamiana:")
        etykieta3 = QLabel("Wynik: ")
        etykietaPREC = QLabel("Miejsc po przecinku ")

        # pola edycyjne
        self.liczba1 = QLineEdit()
        self.okno2 = QLineEdit()
        self.wynik = QLineEdit()
        self.wynik.setEnabled(False)
        self.okno2.setEnabled(False)
        self.wynik.setToolTip('Wpisz <b>wartość</b> i wybierz jednostki..')
        self.wynikd = QLineEdit()   #pole niewidoczne dla użytkownika, przechowuje dokładny wynik

        # listy rozwijane
        self.listajedn1 = QComboBox(self)
        self.listajedn1.setEnabled(False)
        self.listajedn2 = QComboBox(self)
        self.listajedn2.setEnabled(False)

        # pole przewijane
        self.spinPREC = QSpinBox()
        self.spinPREC.setMinimum(0)
        self.spinPREC.setMaximum(10)
        self.spinPREC.setSingleStep(1)
        self.spinPREC.setValue(3)
        self.spinPREC.setEnabled(False)

        # slider i LCDNumber
        self.suwak = QSlider(Qt.Horizontal)
        self.suwak.setMinimum(0)
        self.suwak.setMaximum(10)
        self.suwak.setEnabled(False)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        # ukłąd tabelaryczny
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta0,0,1)
        ukladT.addWidget(etykieta1, 2,0)
        ukladT.addWidget(etykieta01, 4, 0)
        ukladT.addWidget(etykieta11,4,2)
        ukladT.addWidget(etykieta2, 2, 1)
        ukladT.addWidget(etykieta3, 2, 2)
        ukladT.addWidget(etykietaPREC,6,0)
        ukladT.addWidget(self.liczba1, 3, 0)
        ukladT.addWidget(self.okno2, 3, 1)
        ukladT.addWidget(self.wynik, 3, 2)
        ukladT.addWidget(self.spinPREC, 6,1)
        ukladT.addWidget(self.suwak,7,1)
        ukladT.addWidget(self.lcd,7,2)

        # przyciski
        OKBtn = QPushButton("&OK", self)
        koniecBtn = QPushButton("&Koniec", self)
        dlugoscBtn = QPushButton("&Długość", self)
        predkoscBtn = QPushButton("&Prędkość", self)
        tempBtn = QPushButton("&Temperatura", self)
        mocBtn = QPushButton("&Moc", self)

        #opisy przyciskow
        dlugoscBtn.setToolTip('Dostępne jednostki: <b><i>km,m,dm,cm,mm</i></b>')
        predkoscBtn.setToolTip('Dostępne jednostki: <b><i>km/h,m/s</i></b>')
        tempBtn.setToolTip('Dostępne jednostki: <b><i>*C, K, F</i></b>')
        mocBtn.setToolTip('Dostępne jednostki: <b><i>KM,W</i></b>')
        koniecBtn.setToolTip('Kliknij, aby wyjść z programu')

        # wiersz, kolumna, ilosc wierszy, ilosc kolumn
        ukladH = QHBoxLayout()
        ukladH.addWidget(dlugoscBtn)
        ukladH.addWidget(predkoscBtn)
        ukladH.addWidget(tempBtn)
        ukladH.addWidget(mocBtn)
        ukladT.addLayout(ukladH, 1, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 8, 0, 1, 3)
        ukladT.addWidget(OKBtn,6,2,1,1)
        uklad = QVBoxLayout()
        ukladT.addWidget(self.listajedn1,5,0)
        ukladT.addWidget(self.listajedn2,5,2)

        self.setLayout(ukladT)

        # obsługa zdarzeń
        koniecBtn.clicked.connect(self.koniec)
        OKBtn.clicked.connect(self.dzialanie)
        dlugoscBtn.clicked.connect(self.wypelnianielist)
        dlugoscBtn.clicked.connect(self.dzialanie)
        predkoscBtn.clicked.connect(self.wypelnianielist)
        predkoscBtn.clicked.connect(self.dzialanie)
        tempBtn.clicked.connect(self.wypelnianielist)
        tempBtn.clicked.connect(self.dzialanie)
        mocBtn.clicked.connect(self.wypelnianielist)
        mocBtn.clicked.connect(self.dzialanie)
        self.suwak.valueChanged.connect(self.warsuw)


        self.resize(300, 150)
        self.setWindowTitle("Konwerter jednostek")
        self.show()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def koniec(self):
        self.close()

    def wypelnianielist(self):
        nadawca = self.sender()
        self.listajedn1.clear()
        self.listajedn2.clear()
        if nadawca.text() == "&Długość":
            for v in ('km','m','dm', 'cm', 'mm'):
                self.listajedn1.addItem(v)
                self.listajedn2.addItem(v)
        elif nadawca.text() == "&Prędkość":
            for v in ('km/h','m/s'):
                self.listajedn1.addItem(v)
                self.listajedn2.addItem(v)
        elif nadawca.text() == "&Temperatura":
            for v in ('*C','K', 'F'):
                self.listajedn1.addItem(v)
                self.listajedn2.addItem(v)
        elif nadawca.text() == "&Moc":
            for v in ('KM','W'):
                self.listajedn1.addItem(v)
                self.listajedn2.addItem(v)
        self.listajedn1.setEnabled(True)
        self.listajedn2.setEnabled(True)
        self.spinPREC.setEnabled(True)



    def dzialanie(self):
        nadawca = self.sender()
        wartosc1 = self.listajedn1.currentText()
        wartosc2 = self.listajedn2.currentText()
        prec=self.spinPREC.value()

        try:
            if nadawca.text() == "&OK":
                liczba = float(self.liczba1.text())
                if liczba < 0:
                    if wartosc1 != "*C":
                        if wartosc1!="K":
                            if wartosc1!= "F":
                                QMessageBox.warning(self, "Błąd", "Błędna wartość!", QMessageBox.Ok)
                                liczba = 0
                zamiana = wartosc1 + "--->" + wartosc2
                self.okno2.setText(str(zamiana))

                if wartosc1 == wartosc2:  # najprostszy przypadek
                    wynik = liczba

                if wartosc1 == "km":  # konwercja długości
                    if wartosc2 == "m":
                        wynik = liczba * 1000
                    elif wartosc2 == "dm":
                        wynik = liczba * 10000
                    elif wartosc2 == "cm":
                        wynik = liczba * 100000
                    elif wartosc2 == "mm":
                        wynik = liczba * 1000000
                elif wartosc1 == "m":
                    if wartosc2 == "km":
                        wynik = liczba / 1000
                    elif wartosc2 == "dm":
                        wynik = liczba * 10
                    elif wartosc2 == "cm":
                        wynik = liczba * 100
                    elif wartosc2 == "mm":
                        wynik = liczba * 1000
                elif wartosc1 == "dm":
                    if wartosc2 == "km":
                        wynik = liczba / 10000
                    elif wartosc2 == "m":
                        wynik = liczba / 10
                    elif wartosc2 == "cm":
                        wynik = liczba * 10
                    elif wartosc2 == "mm":
                        wynik = liczba * 100
                elif wartosc1 == "cm":
                    if wartosc2 == "km":
                        wynik = liczba / 100000
                    elif wartosc2 == "m":
                        wynik = liczba / 100
                    elif wartosc2 == "dm":
                        wynik = liczba / 10
                    elif wartosc2 == "mm":
                        wynik = liczba * 10
                elif wartosc1 == "mm":
                    if wartosc2 == "km":
                        wynik = liczba / 1000000
                    elif wartosc2 == "m":
                        wynik = liczba / 1000
                    elif wartosc2 == "dm":
                        wynik = liczba / 100
                    elif wartosc2 == "cm":
                        wynik = liczba / 10

                if wartosc1 == "km/h":  # konwercja predkosci
                    if wartosc2 == "m/s":
                        wynik = liczba / 3.6
                elif wartosc1 == "m/s":
                    if wartosc2 == "km/h":
                        wynik = liczba * 3.6

                if wartosc1 == "KM":  # konwercja mocy
                    if wartosc2 == "W":
                        wynik = liczba * 735.49875
                if wartosc1 == "W":
                    if wartosc2 == "KM":
                        wynik = liczba / 735.49875

                if wartosc1 == "*C":
                    if wartosc2 == "K":
                        wynik = liczba + 273.15
                    elif wartosc2 == "F":
                        wynik = 1.8*liczba + 32
                elif wartosc1 == "K":
                    if wartosc2 == "*C":
                        wynik = liczba - 273.15
                    elif wartosc2 == "F":
                        wynik = 1.8 * (liczba - 273.15) + 32
                elif wartosc1 =="F":
                    if wartosc2 == "K":
                        wynik = (0.5555555*(liczba-32) +273.15)
                    elif wartosc2 == "*C":
                        wynik = 0.5555555*(liczba-32)



                self.wynik.setText(str(round(wynik,prec)))
                self.wynikd.setText(str(wynik))
                self.lcd.display(prec)
                self.spinPREC.setValue(prec)
                self.suwak.setValue(prec)
                self.suwak.setEnabled(True)
                self.suwak.setValue(prec)

        except (ValueError, ZeroDivisionError):
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.Ok)


    def warsuw(self):
        prec=self.suwak.value()
        wynik=float(self.wynikd.text())
        self.wynik.setText(str(round(wynik,prec)))
        self.lcd.display(prec)
        self.spinPREC.setValue(prec)


if __name__ == '__main__':
    import sys

    app=QApplication(sys.argv)
    okno=Konwerter()
    sys.exit(app.exec_())
