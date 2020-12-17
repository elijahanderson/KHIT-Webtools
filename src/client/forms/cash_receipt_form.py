from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class CashReceiptForm(FlaskForm):
    file = FileField('Select cash receipt report to modify: ',
                     validators=[FileRequired(), FileAllowed(['csv', 'xlsx'], 'File must end in .csv or .xlsx')])
    upload = SubmitField('Upload')
