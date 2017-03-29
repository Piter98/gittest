#!/usr/bin/env python
# -*- coding: utf-8 -*-
#wersja obiektowa
import sys
#Definicja klasy
class Samochod(object):
    def __init__(self,marka,model,ladownosc,ileOsob=0):
        self.marka = marka
        self.model = model
        self.ladownosc = ladownosc
        self.ileOsob=ileOsob

    def laduj(self, ile):
        if self.ileOsob + ile > self.ladownosc:
            print "Brak miejsc!"
        else:
            self.ileOsob+= ile
            return Samochod.ileOsob

    def wyladuj(self, ile):
        if self.ileOsob - ile < 0:
            print "Nie ma tylu osob!"
        else:
            self.ileOsob-= ile
            return Samochod.ileOsob


samochod1 = Samochod('Range Rover', 'Evoque', 9)
#samochod1.laduj(8)





sys.exit()

osoba1 = Konto(100)#instancja klasy konto
osoba2 = Konto()

ile = int(raw_input("Wpłata 1: "))
print "Stan konta:", osoba1.wplata(ile)

ile = int(raw_input("Wpłata 2: "))
print "Stan konta:", osoba2.wplata(ile)

ile = int(raw_input("Wypłata 1: "))
print "Stan konta:", osoba1.wyplata(ile)

ile = int(raw_input("Wypłata 2: "))
print "Stan konta:", osoba2.wyplata(ile)
