from flask import Blueprint, render_template, request

from src.client.forms.isl_form import ISLForm
from src.infrastructure.isl_rpa import isl


isl_rpa_blueprint = Blueprint('isl_rpa_views', __name__, template_folder='templates')


@isl_rpa_blueprint.route('/isl-rpa', methods=['GET', 'POST'])
def isl_rpa():
    form = ISLForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            isl(form.from_date.data)
            return render_template('isl_rpa.html', title='ISL Automation', form=form)
    return render_template('isl_rpa.html', title='ISL Automation', form=form)
