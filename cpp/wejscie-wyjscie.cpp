/*
 * wejscie-wyjscie.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */


#include <iostream>
#include <iomanip>
#include <cstdio>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int lint = 0;
    cout << "Podaj liczbę całkowitą: ";
    cin >> lint;

    cout.setf(ios_base::hex, ios_base::basefield);
    cout.setf(ios_base::showbase);
    cout << "Hex: " << lint <<endl;

    cout.setf(ios_base::oct, ios_base::basefield);
    cout.setf(ios_base::showbase);
    cout << "Oct: " << lint <<endl;

	return 0;
}

