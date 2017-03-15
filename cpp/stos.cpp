/*
 * stos.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */


#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

void push(int stos[], int &sp, int dane)
{
    cout << dane << " ";
    stos[sp] = dane;
    sp ++;
}

int pop(int stos[], int &sp)
{
    sp--;
    return stos[sp];
}

int main(int argc, char **argv)
{
    int *stack;// wskaźnik stosu
    int sr; // rozmiar stosu
    int sp =0; // wskaźnik stosu

    cout << " Podaj rozmiar: ";
    cin >>sr;
    if (!cin)
        {
        cout << "Błędne dane!";
        return -1;
        }
    stack = new int[sr];

    for(int i =0; i<sr; i++)
        push(stack,sp, rand()%100 + 1); // wstaw na stos
    //push(stack,sp, 101);
    //cout << stack[0] << " " << stack[1];;
    cout << endl;
    for(int i =0; i<sr; i++)
        cout << pop (stack, sp) << " ";  // zdejmij ze stosu
    //cout << pop (stack,sp) << " ";
	return 0;
}

