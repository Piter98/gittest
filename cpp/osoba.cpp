/*
 * osoba.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */

#include <iostream>
#include <fstream>

using namespace std;

struct osoba {
    char imie[20];
    char nazwisko[25];
    int wiek;
};

void pobierzDane(osoba tb[], int ile)
    {
    for (int i=0; i<ile; i++)
        {
        cout << "Imie: " ; cin >> tb[i].imie;
        cout << "Nazwisko: " ; cin >> tb[i].nazwisko;
        cout << "Wiek: " ; cin >> tb[i].wiek;
        cout << endl;
        }
    }

void wyswietlDane(osoba tb[], int ile)
    {
    for (int i=0; i<ile; i++)
        {
        cout << "Imie: " << tb[i].imie <<endl;
        cout << "Nazwisko: "<< tb[i].nazwisko<<endl;
        cout << "Wiek: "<<tb[i].wiek<<endl;
        cout << endl;
        }
    }

void zapiszDane(osoba tb[], int ile)
{
    ofstream uPliku; //uchwyt pliku
    uPliku.open("osoby.csv");
    for (int i=0; i<ile; i++)
    {
        uPliku << tb[i].imie << "," << tb[i].nazwisko<< ","<<tb[i].wiek<<"\r\n";
    }
    uPliku.close();
    cout << "Zapisano!"<<endl;
}

void czytajDane(osoba tb[])
{
    ifstream plik("osoby.csv");
    if (!plik.is_open())
    {
        cout << "Bład otwarcia pliku!";
        //return 1;
    }
}

int main(int argc, char **argv) {
    int ile =0;
    cout << "Ile osób?";
    cin >> ile;

    osoba *tbOsoby = new osoba[ile];
    pobierzDane(tbOsoby, ile);
    wyswietlDane(tbOsoby, ile);
    zapiszDane(tbOsoby, ile);
    czytajDane(tbOsoby);
	return 0;
}

