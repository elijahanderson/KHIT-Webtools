from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class DPNForm(FlaskForm):
    file = FileField('Select DPN report to modify:  ',
                     validators=[FileRequired(), FileAllowed(['csv', 'xls'], 'File must end in .csv or .xls')])
    upload = SubmitField('Upload')
