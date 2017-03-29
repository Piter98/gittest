#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3  # import modułu do obsługi baz

plik = "baza.db"  # nazwa pliku z bazą
baza = sqlite3.connect(plik)  # połaczenie z bazą
baza.row_factory = sqlite3.Row #ustawienie sposobu dostępu do pól rekordów

with baza:
    kursor = baza.cursor()  #utworzenie obiektu kursora
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

INSERT INTO pracownicy VALUES (NULL, "Jan", "Kowalski", "27-600", "Sandomierz", "Matejki 2/3", date("1968-12-22"), "Tarnobrzeg");
INSERT INTO pracownicy VALUES (NULL, "Anna", "Nowak", "27-610", "Sandomierz", "Miła 2/3", date("1970-12-04"), "Sandomierz");
INSERT INTO kontakty VALUES (NULL, "1", "0", "601-324-657", "komórka");
INSERT INTO kontakty VALUES (NULL, "2", "0", "624-98-00", "stacjonarny");
INSERT INTO stanowiska VALUES (NULL, "dyrektor");
INSERT INTO stanowiska VALUES (NULL, "asystentka");
INSERT INTO stanowiska VALUES (NULL, "ksiegowa");
INSERT INTO stanowiska VALUES (NULL, "serwisant");
INSERT INTO place VALUES ("1","1", 3500, date("1992-12-03"));
INSERT INTO place VALUES ("2","3", 2300, date("1993-02-01"));
    """)

#słownik zawierajacy dane do wstawienia do bazy
dane = {
    'pracownicy' : [(('Jan'), ('Kowalski'), ('27-600'), ('Sandomierz'), ('1968-12-02'))],
    'kontakty' : [(1, "0", ('445-885-965'), ('komórkowy'))],
}


def lista(tabela, pola):
    kursor.execute('SELECT * FROM %s' % tabela)
    wynik = kursor.fetchall()
    for rekord in wynik:
        for pole in pola:
            print rekord[pole],
        print

# sprawdzamy, czy zostały dodane dane
#klauzula SELECT


#kursor.execute('SELECT * FROM kontakty')
#wynik = kursor.fetchall()
#for rekord in wynik:

#    print rekord['idPracownika'], rekord ['kontakt'], rekord ['uwagi']
# dodanie nowego pracownika
lista('kontakty', ('kontakt','uwagi'))
imie = raw_input('Podaj imie pracownika: ')
nazwisko = raw_input('Podaj nazwisko pracownika: ')
#print imie, nazwisko
kursor.execute('INSERT INTO pracownicy (imie, nazwisko) VALUES(?, ?)', (imie.decode('utf-8'), nazwisko.decode('utf-8')))
#kursor.execute('SELECT * FROM pracownicy')
#wynik = kursor.fetchall()
#for rekord in wynik:
#    print rekord['imie'], rekord ['nazwisko']

lista('pracownicy',('imie','nazwisko'))
baza.commit()  # zatwierdzenie zmian w bazie
baza.close()
