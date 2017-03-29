#!/usr/bin/env python
# -*- coding: utf-8 -*-
#wersja linearna, zmienna globalna
bilans = 0 #zmienna globalna

ile = int(raw_input("Wpłata: "))
bilans += ile
print "Stan konta:", bilans

ile = int(raw_input("Wyłata: "))
bilans -= ile
print "Stan konta:", bilans
