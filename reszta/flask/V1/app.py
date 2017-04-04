# -*- coding: utf-8 -*-
# quiz_pw/app.py

from flask import Flask, g
from flask import render_template, request, redirect, url_for, flash
from models import *
from dane import *
from forms import *

app = Flask(__name__)

# konfiguracja aplikacji, m.in. klucz do obsługi sesji HTTP wymaganej
# przez funkcję flash
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    TYTUL='Quiz'
))

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loguj')
def loguj():
    tresc = '<h1>Zaloguj się!</h1>'
    return tresc

@app.route('/edycja', methods = ['GET'])
def edycja():
    #adres = '<a href="'+url_for('edytuj', pid=0)+'">Przejdź tu!</a>'
    #return adres
    return render_template("edycja.html")

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    pytania = Pytanie.select()
    if not pytania.count():
        return redirect(url_for('index'))
    if request.method == 'POST':
        punkty = 0
        for nrpyt, odp in request.form.items():
            odpok = Pytanie.select(Pytanie.odpok).where(Pytanie.id == int(nrpyt)).scalar()
            if odp == odpok:
                punkty += 1
        flash("Wynik: %s" % punkty)
    return render_template('quiz.html', dane = pytania)

@app.route('/edytuj/<int:pid>',methods = ['GET', 'POST'])
def edytuj(pid):
    form = DodajForm()
    if pid:
        pyt = Pytanie.select().annotate(Odpowiedz).where(Pytanie.id==pid).get()
        for i in range(3):#wyszukuje indeks poprawnej odpowiedzi
            if pyt.odpok == pyt.odpowiedzi[i].odpowiedz:
                break

        form = DodajForm(odpok=str(i))
        form.pytanie.data = pyt.pytanie
        form.odp0.data = pyt.odpowiedzi[0].odpowiedz
        form.odp1.data = pyt.odpowiedzi[1].odpowiedz
        form.odp2.data = pyt.odpowiedzi[2].odpowiedz
        form.pid.data = pyt.id

    if form.validate_on_submit():
        pid = form.pid.data
        pyt = Pytanie.select().annotate(Odpowiedz).where(Pytanie.id==pid).get()
        pyt.pytanie = form.pytanie.data
        odp = [form.odp0.data, form.odp1.data, form.odp2.data]
        odpok = odp[int(form.odpok.data)]
        pyt.odpok = odpok
        pyt.save()
        for indeks, o in enumerate(pyt.odpowiedzi):
            o.odpowiedz = odp[indeks]
            o.save()
        flash("Zaaktualizowano pytanie: %s " % form.pytanie.data)
       # return redirect(url_for('quiz'))

    pytania = Pytanie().select()
    return render_template("edytuj.html", pytania=pytania, form=form, radio=list(form.odpok))

@app.route('/usun/<int:pid>',methods = ['GET', 'POST'])
def usun(pid):
    pyt = Pytanie.get(Pytanie.id==pid)
    pyt.delete_instance(recursive=True)
    flash("Usunięto pytanie")
    return redirect(url_for('index'))


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Błąd: %s. Pole: %s" % (
                error,
                getattr(form, field).label.text
            ))

@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    form = DodajForm()
    if form.validate_on_submit():
        odp = [form.odp0.data, form.odp1.data, form.odp2.data]
        odpok = odp[int(form.odpok.data)]
        pyt = Pytanie(pytanie=form.pytanie.data, odpok=odpok)
        pyt.save()
        for o in odp:
            ins = Odpowiedz(pnr=pyt.id, odpowiedz=o)
            ins.save()
        flash("Dodano pytanie: %s " % form.pytanie.data)
        return redirect(url_for('quiz'))
    else:#dane błedne
        flash_errors(form)

    return render_template('dodaj.html', form=form, radio=list(form.odpok))

if __name__ == '__main__':
    import os
    if not os.path.exists('quiz.db'):
        baza.create_tables([Pytanie, Odpowiedz], True)  # tworzymy tabele
        dane = pobierz_dane("pytania.csv")
        dodaj_pytania(dane)
        print dane
    app.run(debug=True)
