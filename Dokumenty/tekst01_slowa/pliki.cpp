#include <iostream>
#include <cstring>
using namespace std;


bool czy_palindrom(char tab[]) {
    int rozmiar = strlen(tab);
    cout<< rozmiar;
    bool czypalindron = true;
    for(int i = 0; i < rozmiar / 2; i++) {
        cout << tab[i] << " " << tab[rozmiar - 1 - i];
        if(tab[i] != tab[rozmiar - 1 - i])
        czypalindron = false;
    }
    return czypalindron;
}

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


int main(int argc, char **argv) {

    string dane[1000];
    string npliku ("dane2006.txt");
    cout << "Otwieram plik "<< npliku<<endl;
    ifstream plik(npliku.c_str());
    string linia;
    if(!plik) return 0;
    //int i=-1;
    while(!plik.eof())
        {
        getline(plik, linia);
        if (czy_palindrom(tab))
            cout << "to palindrom";
        else
            cout << "To nie jest palindrom";
        }
	return 0;
}
