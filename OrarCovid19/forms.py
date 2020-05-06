from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, length
from wtforms.fields.html5 import DateTimeLocalField

class AddForm(FlaskForm):
    Password=PasswordField('Parola Admin', validators=[DataRequired()])
    Materie=StringField('Materie', validators=[DataRequired()])
    start_date=DateTimeLocalField('Data si ora', format='%Y-%m-%d %H:%M', validators=[DataRequired()])

    submit=SubmitField('Adauga!')