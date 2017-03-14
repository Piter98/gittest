/*
 * wskazniki.cpp
 * Copyright 2017 user <user@lap79>
 * wskaźniki i dynamiczne struktury danych
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    //~int x= 11;
    //~cout << x << endl; //wartość
    //~cout << &x << endl; //adres
    //~cout << sizeof(x) << endl; //rozmiar w pamięci

    //~int *intPtr;
    //~intPtr =&x;
    //~cout << intPtr <<endl;
    //~cout << *intPtr <<endl; //dereferencja
    //~*intPtr += *intPtr;
    //~cout << *intPtr <<endl;
    //~intPtr+=1; // inkrementacja wskaznika, powiekszenie
    //~cout <<  intPtr <<endl;

    int *tbIntPtr=NULL;
    int tab [100];
    cout << tab <<endl;
    int ile = 0;
    cout << "Ile liczb podasz?" <<endl;
    cin >> ile;
    tbIntPtr = new int[ile];
    cout << tbIntPtr <<endl;
    cout << "Poaj liczby: "<<endl;
    for (int i = 0; i<ile; i++)
        cin >> tbIntPtr[i];
    cout << *tbIntPtr<<endl;

    return 0;
}

