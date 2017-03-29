# -*- coding: utf-8 -*-
from peewee import *

# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('quiz.db')

class BaseModel(Model):
    class Meta:
        database = baza


class Pytanie(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()


class Odpowiedz(BaseModel):
    pnr = ForeignKeyField(
        Pytanie, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
