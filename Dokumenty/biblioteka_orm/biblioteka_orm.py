#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

pbaza = 'biblioteka.db'
if os.path.exists(pbaza):
    os.remove(pbaza)
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase(pbaza)  # ':memory:'

# BazaModel to klasa bazowa dla klas Klasa i Uczen, które
# opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi


class BazaModel(Model):
    class Meta:
        database = baza

class Rodzaj(BazaModel):
    rodzaj = CharField(null=False)

class Ksiazka(BazaModel):
    imiona = CharField(null=False)
    nazwisko = CharField(null=False)
    tytul = TextField()
    wydawnictwo = CharField()
    miejscowosc_wyd = CharField()
    data_wyd = DateField()
    cena = FloatField()
    rodzaj = ForeignKeyField(Rodzaj, related_name='rodzaje')


baza.connect()  # nawiązujemy połączenie z bazą
# tworzymy tabele
baza.create_tables([Ksiazka, Rodzaj], True)

def utworzRodzaj(dane):
    inst_rodzaj = Rodzaj(rodzaj=dane[0])
    inst_rodzaj.save()
utworzRodzaj(('epika',))
utworzRodzaj(('liryka',))
utworzRodzaj(('dramat',))

def utworzKsiazke(dane):
    inst_rodzaj = Rodzaj.select().where(Rodzaj.rodzaj == dane[7]).get()
    inst_ksiazka = Ksiazka(imiona=dane[0], nazwisko=dane[1], tytul=dane[2], wydawnictwo=dane[3], miejscowosc_wyd=dane[4], data_wyd=dane[5], cena=dane[6], rodzaj=inst_rodzaj)
    inst_ksiazka.save()
utworzKsiazke(('Tadeusz','Różewicz', 'Kartoteka','Wydawnictwo Literackie','Kraków', 2003, 34.99, 'epika'))
# przykłady kwerend
# Przyklad.select().where(Przyklad.pole_tekst == 'tekst')
# Przyklad.select().where(Przyklad.pole_tekst == 'tekst', Przyklad.pole_logiczne == True)




#inst_zadanie=Ksiazka.select(imiona, nazwisko, tytul, rodzaj).where(Ksiazka.nazwisko='Białoszewski')
A = Ksiazka.select().where(Ksiazka.nazwisko=='Różewicz')
for el in A:
        print el.nazwisko, el.imiona, el.tytul, el.rodzaj.rodzaj

B = Ksiazka.select().where(Ksiazka.data_wyd==2000)
for ele in B:
    print ele.nazwisko, ele.imiona, ele.tytul, ele.data_wyd

C= Ksiazka.select().where(Ksiazka.wydawnictwo== 'Państwowy Instytut Wydawniczy')
for elo in C:
    print elo.nazwisko, elo.imiona, elo.tytul, elo.wydawnictwo

D= Ksiazka.select().join(Rodzaj).where(Rodzaj.rodzaj == 'Liryka')
for eli in D:
    print eli.imie, eli.nazwisko, eli.tytul
