from flask_wtf import FlaskForm

from wtforms import IntegerField, SubmitField, validators


class AbilityToPayForm(FlaskForm):
    income = IntegerField('Monthly Gross Income:  ',
                          validators=[validators.required('Please enter valid income value'),
                                      validators.number_range(min=0, message='Income must be a positive integer')])
    size = IntegerField('Household Family Size:  ',
                        validators=[validators.required('Please enter valid family size'),
                                    validators.number_range(min=1, message='Family size must be a positive, '
                                                                           'non-zero integer')])
    extra_expenses = IntegerField('Extraordinary Expenses:  ',
                                  validators=[validators.optional(),
                                              validators.number_range(min=0,
                                                                      message='Extraordinary expenses must be a '
                                                                              'positive integer')])

    submit = SubmitField('Submit')
