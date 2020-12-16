from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class CashReceiptForm(FlaskForm):
    file = FileField('Upload',
                     validators=[FileRequired(), FileAllowed(['csv', 'xlsx'], 'File must end in .csv or .xlsx')])
