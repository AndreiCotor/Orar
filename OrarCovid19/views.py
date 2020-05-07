"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,redirect,request,url_for
from OrarCovid19 import app,db
from OrarCovid19.forms import AddForm,DeleteForm
from OrarCovid19.database import postare

db.create_all()

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

    ore=postare.query.all()
    ore=sorted(ore, key=lambda postare: postare.date)

    return render_template('index.html',title='Următorele',year=datetime.now().year,ore=ore)


@app.route('/add',methods=['GET','POST'])
def add():
    form=AddForm()

    if form.validate_on_submit() and form.Password.data=="bagpula1":
        curs=postare(subject=form.Materie.data,date=form.start_date.data)
        db.session.add(curs)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html',title='Adaugă',year=datetime.now().year,form=form)

@app.route("/<int:post_id>",methods=['GET','POST'])
def delete(post_id):
    post=postare.query.get_or_404(post_id)
    form=DeleteForm()

    if form.validate_on_submit() and form.Password.data=="bagpula1":
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('delete.html',title='Stergere',year=datetime.now().year,form=form)