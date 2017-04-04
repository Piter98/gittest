# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField
from wtforms.validators import Required


class DodajForm(FlaskForm):
    pytanie = StringField(u'Treść pytania:', validators=[Required()])
    odp0 = StringField(u'Odp1', validators=[Required()])
    odp1 = StringField(u'Odp2', validators=[Required()])
    odp2 = StringField(u'Odp3', validators=[Required()])
    odpok = RadioField(
            u'Poprawna odpowiedź',
            validators=[Required()],
            choices=[('0','o0'),('1','o1'),('2','o2')]
            )
    pid = HiddenField()
