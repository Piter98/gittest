/*
 * formatowanie.cpp
 *
 * Copyright 2017 user <user@lap79>
 * Formatowanie wyjścia, aliasy typu
 * używanie string
 */


#include <iostream>
#include <cstdio> // printf
#include <iomanip>
#include <math.h> // liczba Pi
#include <string>
using namespace std;

int main(int argc, char **argv)
{
    int liczba = 255;

    ios_base::fmtflags fx;
    fx |= cout.oct;
    fx |= cout.showbase;
    cout.flags(fx);
    cout << liczba <<endl;

    cout.setf(ios_base::hex, ios_base::basefield);
    cout.setf(ios_base::showbase);
    cout.setf(ios_base::uppercase);
    cout << liczba <<endl;

    printf("%#x\n",liczba);
    printf("%#o\n",liczba);
    printf("%10.4f\n",M_PI);
    printf("%.6f\n",M_PI);

    typedef string str;
    str tekst;
    cout << "Podaj tekst: ";
    getline(cin, tekst);
    cout.setf(ios_base::dec, ios_base::basefield);
    cout << "Rozmiar: " <<tekst.size() << endl;
    for (unsigned int i =0; i<tekst.size(); i++) {
        cout << (int)tekst[i] <<" ";
        if (tekst[i] == ' ')
            cout<<"Spacja!";
        }

	return 0;
}

