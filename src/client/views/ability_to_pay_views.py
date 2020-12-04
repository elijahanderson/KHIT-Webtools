from flask import Blueprint, render_template, request

from client.forms.ability_to_pay_form import AbilityToPayForm
from infrastructure.ability_to_pay import max_monthly_fee

ability_to_pay_blueprint = Blueprint('ability_to_pay_views', __name__, template_folder='templates')


@ability_to_pay_blueprint.route('/ability-to-pay', methods=['GET', 'POST'])
def ability_to_pay():
    """ REST endpoint for the ability to pay calculator. """
    form = AbilityToPayForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            income = form.income.data
            size = form.size.data
            extra_expenses = form.extra_expenses.data if form.extra_expenses.data else 0
            fee = 'The maximum monthly fee is $%s' % str(max_monthly_fee(income, size, extra_expenses))
            return render_template('ability_to_pay.html', title='Ability to Pay Calculator', fee=fee, form=form)
    return render_template('ability_to_pay.html', title='Ability to Pay Calculator', form=form)
