"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from OrarCovid19 import app
from OrarCovid19.forms import AddForm

app.config['SECRET_KEY']='asffdnasofsfeeq132th134ri3tbas9r32btrfp93rw3373712931sf'

ore=[
    {
        'subject' : 'Romana',
        'day' : 10,
        'month' : 5,
        'year' : 2020,
        'hour' : 12,
        'minu' : 0
    },
    {
        'subject' : 'Mate',
        'day' : 8,
        'month' : 5,
        'year' : 2020,
        'hour' : 11,
        'minu' : 0
    }
]

def cmp(a,b):
    if a.year!=b.year:
        return numpy.sign(a.year-b.year)
    elif a.month!=b.month:
        return numpy.sign(a.month-b.month)
    elif a.day!=b.day:
        return numpy.sign(a.day-b.day)
    elif a.hour!=b.hour:
        return numpy.sign(a.hour-b.hour)
    else:
        return numpy.sign(a.minu-b.minu)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    """ore.sort(key=cmp)"""

    return render_template(
        'index.html',
        title='Următorele',
        year=datetime.now().year,
        ore=ore
    )


@app.route('/add')
def add():
    form=AddForm()
    return render_template(
        'add.html',
        title='Adaugă',
        year=datetime.now().year,
        form=form
    )
