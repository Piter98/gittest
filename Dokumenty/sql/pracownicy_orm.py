#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

plik = 'pracownicy.db'

if os.path.exists(plik):
    os.remove(plik)
baza = SqliteDatabase(plik)  # instancja bazy używanej przez modele (':memory:')

# BazaModel to klasa bazowa dla klas Klasa i Uczen, które
# opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi

class BazaModel(Model):
    class Meta:
        database = baza

class Pracownik(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    data = DateField()
    miasto = CharField(default='')
    ulica = CharField(default='')
    kod = CharField(default='')
    miejscowosc = CharField(default='')

class Kontakt(BazaModel):
    pracownik = ForeignKeyField(Pracownik, related_name='kontakty')
    typK = IntegerField(default = 1)
    kontakt = CharField(default='')
    uwagi = CharField(default='')

class Stanowisko(BazaModel):
    stanowisko = CharField(null=False)

class Placa(BazaModel):
    pracownik = ForeignKeyField(Pracownik, related_name='place')
    stanowisko = ForeignKeyField(Stanowisko)
    placa = DecimalField()
    dataz = DateTimeField()

class SwiadczenieTyp(BazaModel):
    opis = CharField(null=False)
    kwota = DecimalField(null=False)

class Swiadczenie(BazaModel):
    pracownik = ForeignKeyField(Pracownik, related_name='swiadczenia')
    typ = ForeignKeyField(SwiadczenieTyp)
    data = DateTimeField()

baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Pracownik, Kontakt, Stanowisko, Placa, SwiadczenieTyp, Swiadczenie], True)  # tworzymy tabele

def pobierz_dane(tabela, pola, klasa):
    """
    Funkcja pobiera dane z pliku csv i zwraca w postaci listy tupli
    """
    dane = []  # lista z danymi rekordów
    plik = tabela + ".csv"
    if os.path.isfile(plik):
        with open(plik, "r") as zawartosc:
            for linia in zawartosc:
                linia = linia.replace("\n", "")
                linia = linia.replace("\r", "")
                linia = linia.replace(' "', "")
                linia = linia.replace('"', "")
                linia = linia.decode('utf-8')
                linia = tuple(linia.split(","))
                dane.append(linia)

        for i in range(len(dane)):
            wynik = zip(pola, dane[i])
            objstr = ''
            for el in wynik:
                objstr += el[0] +"='" + el[1] + "', "
            objstr = klasa + '(' + objstr[:-2] +')'
            inst = eval(objstr)
            inst.save()
    else:
        print "Brak pliku!"

pobierz_dane('pracownicy', ("imie", "nazwisko", "kod", "miejscowosc", "ulica", "data", "miasto"), 'Pracownik')
pobierz_dane('kontakty', ('pracownik', 'typK', 'kontakt', 'uwagi'), 'Kontakt')
pobierz_dane('stanowiska', ('stanowisko', ), 'Stanowisko')
pobierz_dane('place', ('pracownik', 'stanowisko', 'placa' , 'dataz'), 'Placa')

#rekordy = Stanowisko.select()
#for r in rekordy:
#    print r.stanowisko

#rekordy = Pracownik.select()
#for r in rekordy:
 #   print r.imie, r.nazwisko

#rekordy = Kontakt.select()
#for r in rekordy:
#    print r.pracownik.nazwisko, r.kontakt

rekordy = Placa.select()
for r in rekordy:
    print r.pracownik.nazwisko, r.pracownik.imie, r.stanowisko.stanowisko, r.placa
