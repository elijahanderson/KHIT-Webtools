from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class CashReceiptForm(FlaskForm):
    file = FileField('Select cash receipt report to modify:  ',
                     validators=[FileRequired(), FileAllowed(['csv', 'xls'], 'File must end in .csv or .xls')])
    upload = SubmitField('Upload')
