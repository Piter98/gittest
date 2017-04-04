/*
 * Paluch_tekst.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */


#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;
#define MAX 1500
int l = 0;
int i = -1;

int wczytaj_dane(string npliku, string *tb)
{
   cout << "Otwieram plik "<< npliku<<endl;
   ifstream plik(npliku.c_str());
   string linia;
   if(!plik) return 0;
   //int i=-1;
   while(!plik.eof())
    {
       getline(plik, linia);
       i++;
       tb[i]=linia;
    }
   return i;
}

bool czyPalindrom(string slowo)
{
    int dl = slowo.length();
    for (int i=0; i<(dl/2);i++)
        if (slowo [i] != slowo[dl - 1 - i])
            return false;
    return true;
}

//int parzysta(string slowo)
//{
     //   if (slowo.length() -1) == "B"
    //    {
    //        parzysta ++;
    //    }
   // return parzysta;
//}


int main(int argc, char **argv)
{
    string dane[1000];
    string npliku ("dane2006.txt");
    int ile_linii;
    //int parzysta = 0;
    ile_linii = wczytaj_dane(npliku,dane);
    cout <<"Ilość linii: " << ile_linii<<endl;
    //parzysta(dane);
    //cout << parzysta(dane)
    int p = 0;
    for (int i=0; i<ile_linii;i++)
    {
        if(czyPalindrom(dane[i]))
            p ++;
    }
    cout << "Ilość palindromów: "<<p<<endl;
    return 0;
}

