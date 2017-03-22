/*
 * pliki.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
#define MAX_NAZWA 100

void zapisz_znaki(char *plik)
{
    ofstream f;
    char c;
    f.open(plik);
    do
    {
        c = cin.get();
        if (c!=27)
        {
            //cout <<c;
            f << c;
        }
    }
    while(c != 27);

    f.close();
    cout <<endl;
}

void zapisz_linie(char *plik)
{
    ofstream f;
    string linia;
    f.open(plik, ios::app);
    do
    {
        getline(cin, linia);
        f << linia << "\n";
    }
    while(linia.length() > 1);

    f.close();
    cout <<endl;
}


void czytaj_linie(char *plik)
{
    ifstream f;
    string linia;
    f.open(plik);
    if (f.is_open())
    {
        while(getline(f,linia))
        {
            cout << linia << endl;
        }
        f.close();
    }
    else
        cout << "Brak pliku!";

    cout <<endl;
}


int czytaj_znaki(char *plik)
{
    ifstream f;
    char c;
    int i=0;
    f.open(plik, ios::binary);
    while(!f.eof())
    {
        f >> c;
        cout << c;
        i++;
    }
    f.close();
    cout << endl;
    return i;
}

int main(int argc, char **argv)
{
    char nazwa[MAX_NAZWA];
    cout << "Podaj nazwę pliku: ";
    cin.getline(nazwa, MAX_NAZWA);

    //zapisz_znaki(nazwa);
    zapisz_linie(nazwa);
    cout << "Ilość znaków: " << czytaj_znaki(nazwa)<<endl;
    czytaj_linie(nazwa);
	return 0;
}

