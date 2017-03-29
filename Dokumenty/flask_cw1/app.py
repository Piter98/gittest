# -*- coding: utf-8 -*-
# todo/app.py

from flask import Flask, g
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime
from models import *


app = Flask(__name__)  # obiekt aplikacji

# ustawienia aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    TYTUL=u'Do zrobienia'
))


@app.before_request
def before_request():
    g.db = baza
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


#TODO: Poniżej zdefiniuj widoki
#~@app.route("adres")
#~def funkcja():
    #~return pass
@app.route("/zadania",methods = ['GET'])
def zadania():
    zadania = Zadanie().select()
    return render_template('zadania.html', zadania = zadania)

@app.route("/index",methods = ['GET', 'POST'])
def index():
    adres = '<a href="'+url_for('zadania')+'">Zobacz</a>'
    tresc="Witaj,"+adres+"listę zadań"
    return tresc


if __name__ == '__main__':
    app.run(debug=True)

