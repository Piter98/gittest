/*
 * lista.cpp
 *
 * Copyright 2017 user <user@lap79>
 */

#include <iostream>

//implementacja konstruktora
Lista::Lista()
{
    header.head = NULL;
    header.tail = NULL;

}
// impl. dek.
Lista::~Lista()
{
    while(header.head != NULL)
        Usun();
}

void Lista:Dodaj(int value)
{
    ELEMENT *el = new ELEMENT;
    el->value = value;
    el->next = NULL;
    if (header.head == NULL) // pierwszy element listy
    {
        header.head = el;
        header.tail = el;
    }
    else // kolejny
    {
        header.tail->next = el;
        header.tail = el;
    }
}

void Lista::Wyswietl()
{
    ELEMENT *el = header.head;
    while(el != NULL) //ZAPAMIĘTAĆ!
    {
        cout << el->value<<endl;
        el = el->next;
    }
}

int Lista::Usun()
{
    if(header.head != NULL)
    {
        if(header.head == header.tail)
        {
            int temp = header.head->value;
            delete header.head;
            header.head = NULL;
            header.tail = NULL;
            return temp;
        }
        else // wiele elementów
        {
            ELEMENT *el = header.head;
            while(el->next != header.tail)
            {
                el = el->next;
            }
            int temp = el->next->value;
            delete el-> next;
            el->next = NULL;
            header.tail = el;
            return temp;
        }
    }
    return 0;
}
