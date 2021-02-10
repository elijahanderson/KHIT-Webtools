from flask import Blueprint, render_template, request
from traceback import print_exc

from src.client.forms.isl_form import ISLForm
from src.infrastructure.email import send_gmail
from src.infrastructure.isl_rpa import fremont_isl


isl_rpa_blueprint = Blueprint('isl_rpa_views', __name__, template_folder='templates')


@isl_rpa_blueprint.route('/isl-rpa', methods=['GET', 'POST'])
def isl_rpa():
    form = ISLForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                fremont_isl(form.from_date.data)
            except Exception as e:
                print('System encountered an error running Fremont ISL RPA:\n')
                print_exc()
                email_body = 'System encountered an error running Fremont ISL RPA: %s' % e
                send_gmail('eanderson@khitconsulting.com', 'KHIT Report Notification', email_body)
            return render_template('isl_rpa.html', title='ISL Automation', form=form)
    return render_template('isl_rpa.html', title='ISL Automation', form=form)
