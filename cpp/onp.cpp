/*
 * onp.cxx
 *
 * Copyright 2017 user <user@lap79>
 *
 */

#include <iostream>
#include <string.h>
#include <iomanip>
#include <locale>

using namespace std;

int main(int argc, char **argv)
{
    string onp;
    getline(cin,onp);
    cout << "Podano ciąg: " << onp << endl;

    for(unsigned int i=0; i < onp.size(); i++)
        {
        if (onp[i] == ' ')
            ;
        else if (isdigit(onp[i]))
            cout << "liczba" <<endl;
        else
            cout << "txt";
        }
	return 0;
}

