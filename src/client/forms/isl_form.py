from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ISLForm(FlaskForm):
    from_date = DateField('Date to run: ')
    submit = SubmitField('Submit')
