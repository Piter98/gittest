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
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/usun/<int:pid>',methods = ['GET', 'POST'])
def usun(pid):
    zad = Zadanie.get(Zadanie.id==pid)
    zad.delete_instance(recursive=True)
    #flash(u"Usunięto pytanie")
    return redirect(url_for('zadania.html', zad=zad))


@app.route("/zadania", methods = ['GET', 'POST'])
def zadania():
    zadania = Zadanie.select()
    if request.method == 'POST':

        zadanie = request.form['tresc'].strip()
        if not len(zadanie):
            error.append(u"Brak tresci zadania!")
        else:
            dane_zad = zadanie

            z = Zadanie(tresc=zadanie)
            z.save()

            flash("Dodano zadanie: %s " % tresc)
    return render_template("zadania.html", zadania=zadania)



if __name__ == '__main__':
    app.run(debug=True)
