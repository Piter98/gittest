# -*- coding: utf-8 -*-
# todo/models.py

import os
from peewee import *
from datetime import datetime

# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('todo.db')


class BazaModel(Model):
    class Meta:
        database = baza


### PRZYKŁADY DEFINICJI PÓL
#~ pole_tekst = CharField(null=False, unique=True, default='moj_tekst')
#~ pole_dlugi_tekst = TextField() - dla bardzo długich tekstów
#~ pole_data_czas = DateTimeField(default=datetime.now)
#~ pole_data = DateField()
#~ pole_liczba_calkowita = IntegerField()
#~ pole_liczba_rzeczywista = FloatField()
#~ pole_liczba_dziesietna = DecimalField()
#~ pole_logiczne = BooleanField(default=False)

class Zadanie(BazaModel):
    tresc = TextField()
    datad = DateField(default=datetime.now)
    wykonano = BooleanField(default=False)

if not os.path.exists('todo.db'):
    baza.create_tables([Zadanie], True)
    zad = Zadanie(tresc='Przeczytać granicę')
    zad.save()
    zad = Zadanie(tresc='Powtórzyć antyk')

    baza.commit()
    baza.close()
