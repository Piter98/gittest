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

#TODO: Poniżej zdefiniuj klasę Zadanie i pola: tresc, data_dodania, zrobione
class Zadanie(BazaModel):
    tresc = CharField(unique=True)
    data_dodania = DateTimeField(default=datetime.now)
    zrobione = BooleanField(default=False)

class Meta(BazaModel):
    order_by=['data_dodania']


if not os.path.exists('todo.db'):
    baza.create_tables([Zadanie], True)
    #TODO: Poniżej napisz instrukcje dodające dwa przykładowe zadania
    z = Zadanie(tresc='Przeczytać "Granicę"')
    z.save()
    z = Zadanie(tresc='Powtórzyć antyk')
    z.save()

    baza.commit()
    baza.close()
