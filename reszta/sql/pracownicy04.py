#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3  # import modułu do obsługi baz sqlite3

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

pracownicy = (
    (None, "Jan", "Kowalski", "27-600", "Sandomierz", "Matejki 2/3", "1968-12-22", "Tarnobrzeg"),
    (None, "Anna", "Nowak", "27-610", "Sandomierz", u"Miła 2/3", "1970-12-04", "Sandomierz"),
)
kontakty = (
    (None, 1, "0", "601-324-657", u"komórka"),
    (None, 2, "0", "624-98-00", "stacjonarny"),
)
stanowiska = (
    (None, "dyrektor"),
    (None, "asystentka"),
    (None, u"księgowa"),
    (None, "serwisant"),
)
place = (
    (1, 1, 3500, "1992-12-03"),
    (2, 3, 2300, "1993-02-01"),
)

kursor.executemany('INSERT INTO pracownicy VALUES(?, ?, ?, ?, ?, ?, ?, ?)', pracownicy)
kursor.executemany('INSERT INTO kontakty VALUES(?, ?, ?, ?, ?)', kontakty)
kursor.executemany('INSERT INTO stanowiska VALUES(?, ?)', stanowiska)
kursor.executemany('INSERT INTO place VALUES(?, ?, ?, ?)', place)

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
