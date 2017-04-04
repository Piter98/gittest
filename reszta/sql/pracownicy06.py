#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3  # import modułu do obsługi baz sqlite3
import os
import sys

plik = "baza.db"  # plik z bazą
baza = sqlite3.connect(plik)  # połączenie z bazą
baza.row_factory = sqlite3.Row  # dostęp do pól za pomocą nazw

with baza:
    kursor = baza.cursor()  # utworzenie obiektu kursora
    kursor.executescript("""
DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    kod TEXT,
    miasto TEXT,
    ulica TEXT,
    data DATE,
    miejscowosc TEXT
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idPracownika INTEGER REFERENCES pracownicy(id),
    typK CHAR,
    kontakt TEXT,
    uwagi TEXT
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT
);

DROP TABLE IF EXISTS place;
CREATE TABLE place (
    idPracownika INTEGER REFERENCES pracownicy(id),
    idStanowiska INTEGER REFERENCES stanowiska(id),
    placa FLOAT,
    dataz DATE
);

DROP TABLE IF EXISTS lswiadczen;
CREATE TABLE lswiadczen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opis TEXT,
    kwota FLOAT
);

DROP TABLE IF EXISTS swiadczenia;
CREATE TABLE swiadczenia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idPracownika INTEGER REFERENCES pracownicy(id),
    idKategoria INTEGER REFERENCES lswiadczen(id),
    data DATE
);
    """)

def pobierz_dane(tabela, pola): #funkcja zwraca listę tupil zawierających dane pobrane z podanego pliku
    dane = []  #pusta lista
    plik = tabela +".csv"
    if os.path.isfile(plik):
        with open(plik, "r") as zawartosc: #otwarcie tylko do odczytu jako "zawartosc"
            for linia in zawartosc:
                linia = linia.replace("\n", "")
                linia = linia.replace("\r", "")
                linia = linia.decode('utf-8')
                linia = linia.replace(' "', "")
                linia = linia.replace('"', "")
                linia = linia.split(",")
                dane.append(tuple(linia))
        znaki = "?, " * len(pola)
        sqlstr = 'INSERT INTO ' + tabela + "(" + ",".join(pola) + ") VALUES(" + znaki[0:-2] + ")"
        print
        print sqlstr
        print
        kursor.executemany(sqlstr, dane)
    else:
        print "Brak pliku!"

   #return dane

pobierz_dane('pracownicy', ('imie', 'nazwisko', 'kod', 'miasto', 'ulica', 'data', 'miejscowosc'))
pobierz_dane('kontakty', ('idPracownika', 'typK', 'kontakt', 'uwagi'))
pobierz_dane('stanowiska', ('stanowisko', ))
pobierz_dane('place', ('idPracownika', 'idStanowiska', 'placa' , 'dataz'))
sys.exit()
kursor.executemany('INSERT INTO pracownicy(imie, nazwisko, kod, miasto, ulica, data, miejscowosc) VALUES(?, ?, ?, ?, ?, ?, ?)', pracownicy)
kontakty = pobierz_dane('kontakty')
kursor.executemany('INSERT INTO kontakty(idPracownika, typK, kontakt, uwagi) VALUES(?, ?, ?, ?)', kontakty)
stanowiska = pobierz_dane('stanowiska')
kursor.executemany('INSERT INTO stanowiska, (stanowisko) VALUES(?)', stanowiska)
place = pobierz_dane('place')
kursor.executemany('INSERT INTO place(idPracownika, idStanowiska, placa, dataz) VALUES(?, ?, ?, ?)', place)

#sys.exit() #przerwanie wykonywania skryptu


def lista(tabela, pola):
    """Funkcja wybiera wszystkie rekordy z podanej tabeli
    i wyświetla wskazane pola. Argumenty:
    tabela - nazwa tabeli
    pola - tupla z indeksami lub nazwami pól
    """
    kursor.execute('SELECT * FROM %s' % tabela)
    wynik = kursor.fetchall()
    for rekord in wynik:
        for pole in pola:
            print rekord[pole],
        print

# wywołanie funkcji wyświetlającej dane z tabel
lista('pracownicy', ('imie', 'nazwisko'))
lista('kontakty', ('idPracownika', 'kontakt'))

baza.commit()  # zatwierdzenie zmian w bazie
baza.close()
