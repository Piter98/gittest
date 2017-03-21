/*
 * osoba.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */

#include <iostream>
using namespace std;

struct osoba {
    char imie[20];
    char nazwisko[25];
    int wiek;
};

void pobierzDane(osoba tb[], int ile) {
    for int i=0, i<ile; i++) {
        cout << "Imie: " ; cin >> tb[i].imie;
        cout << "Nazwisko: " ; cin >> tb[i].nazwisko;
        cout << "Wiek: " ; cin >> tb[i].wiek;
        cout << endl;
        }
}


int main(int argc, char **argv) {
    int ile =0;
    cout << "Ile osób?";
    cin >> ile;

    osoba *tbOsoby = new osoba[ile];
    pobierzDane(tbOsoby, ile);

	return 0;
}

