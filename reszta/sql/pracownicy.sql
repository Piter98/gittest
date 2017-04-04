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
