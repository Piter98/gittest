#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('test.db')  # ':memory:'

# BazaModel to klasa bazowa dla klas Klasa i Uczen, które
# opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi


class BazaModel(Model):
    class Meta:
        database = baza
# MODEL
class Klasa(BazaModel):
    klasa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    EgzHum = FloatField()
    EgzMat = FloatField()
    EgzJez = FloatField()

baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Klasa, Uczen], True)  # tworzymy tabele !WAŻNE!

#WSTAWIANIE DANYCH
def utworzKlase(dane):
    inst_klasa = Klasa(klasa=dane[0], roknaboru=dane[1], rokmatury=dane[2])
    inst_klasa.save()
utworzKlase(('1A', 2010,2013))
utworzKlase(('1B', 2010,2013))
utworzKlase(('3A', 2007,2010))

def utworzUcznia(dane):
    inst_klasa = Klasa.select().where(Klasa.klasa == dane[3]).get()
    inst_uczen = Uczen(imie=dane[0], nazwisko=dane[1], plec=dane[2], klasa=inst_klasa, EgzHum=dane[4], EgzMat=dane[5], EgzJez=dane[6])
    inst_uczen.save()
utworzUcznia(('Tomasz', 'Nowak', 'M', '1A', 95,98.5,65))
utworzUcznia(('Adam', 'Kowalski', 'M','1A',87,95,78.5))
utworzUcznia(('Piotr', 'Paluch', 'M', '3A', 85,95,93))
utworzUcznia(('Adam', 'Wolak', 'Niezdecydowany', '3A', 88.8,88.8,88.8))

def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy"""
    for uczen in Uczen.select():  # lub szybsze: Uczen.select().join(Klasa)
        print uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.klasa
    print ""

czytajdane()
# ODCZYTYWANIE DANYCH
def czytajdanek():
    """Funkcja pobiera i wyświetla dane z bazy"""
    for klasa in Klasa.select():  # lub szybsze: Uczen.select().join(Klasa)
        print klasa.id, klasa.klasa, klasa.roknaboru, klasa.rokmatury
    print ""

czytajdanek()

klasa = Klasa.select().where(Klasa.klasa =='1A')
for k in klasa:
    u=k.uczniowie
    for el in u:
        print el.nazwisko

# modyfikacja danych
inst_uczen = Uczen.select().join(Klasa).where(Uczen.nazwisko == 'Nowak').get()
inst_klasa = Klasa.select().where(Klasa.klasa =='1B').get()
inst_uczen.klasa = inst_klasa
inst_uczen.save()

czytajdane()

#USUWANIE DANYCH

inst_uczen = Uczen.select().join(Klasa).where(Uczen.nazwisko == 'Kowalski').get()
inst_uczen.delete_instance()

czytajdane()
