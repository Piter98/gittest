#!/usr/bin/env python
# -*- coding: utf-8 -*-
#wersja obiektowa
import sys
#Definicja klasy
class Konto(object):
    def __init__(self,stan=0):
        self.bilans = stan

    def wplata(self, ile):
        self.bilans+=ile
        return self.bilans

    def wyplata(self, ile):
        self.bilans-=ile
        return self.bilans


### DZIEDZICZENIE
class KontoMinimum(Konto):
    def __init__(self, stan=0, debet=0,dane={}):
        Konto.__init__(self, stan)    #konstruktor rodzica
        self.debet=debet
        self.dane = dane
        #nadpisanie
    def wyplata(self, ile):
        if self.bilans - ile <self.debet:
            print "Brak środków!"
            return self.bilans
        else:
            return Konto.wyplata(self, ile)

    def getDane(self, klucz):
        if klucz in self.dane:
            return self.dane[klucz]
        else:
            print "Brak danych!"
            return False
    def setDane(self, klucz,wartosc):
        self.dane[klucz]=wartosc
        return True

o1_dane={}
#o1_dane['imie'] = raw_input("Imię: ")
o1_dane['imie'] = 'Adam'
#o1_dane['nazwisko'] = 'Miodowy'
osoba1 = KontoMinimum(100,0,o1_dane)#instancja klasy konto
osoba1.setDane('nazwisko', 'Miodowy')
o2_dane={}
o2_dane['imie'] = 'Ewa'
osoba2 = KontoMinimum(0,0,o2_dane)


print osoba1.getDane('nazwisko')
osoba1.setDane('nazwisko', 'Miodowski')
print osoba1.getDane('nazwisko')
print osoba2.getDane('nazwisko')



sys.exit() #zakonczenie skryptu
ile = int(raw_input("Wpłata 1: "))
print "Stan konta:", osoba1.wplata(ile)

ile = int(raw_input("Wpłata 2: "))
print "Stan konta:", osoba2.wplata(ile)

ile = int(raw_input("Wypłata 1: "))
print "Stan konta:", osoba1.wyplata(ile)

ile = int(raw_input("Wypłata 2: "))
print "Stan konta:", osoba2.wyplata(ile)
