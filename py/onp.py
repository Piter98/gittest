#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  onp.py
#
#  Copyright 2017 user <user@lap79>


def main(args):
    stos = []
    onp = raw_input("Podaj wyrażenie: ")
    operand =  ''
    for znak in onp:
        if znak != " " and znak.isdigit():
            operand+=znak
        elif znak == " " and len(operand):
            stos.append(float(operand))
            operand = ""
        elif znak in ('*', '-', '/','+','%'):
            a = str(stos.pop())
            b = str(stos.pop())
            stos.append(eval(b+znak+a))

    print "Wynik: ", stos.pop()
    #wykrywanie bledów
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
