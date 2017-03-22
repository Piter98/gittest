/*
 * pliki.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */


#include <iostream>
#include <fstream>

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

    zapisz_znaki(nazwa);
    cout << "Ilość znaków: " << czytaj_znaki(nazwa)<<endl;

	return 0;
}

