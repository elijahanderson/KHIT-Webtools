import threading

from flask import Blueprint, redirect, render_template, request
from traceback import print_exc

from client.forms.isl_form import ISLForm
from infrastructure.email import send_gmail
from infrastructure.isl_rpa import fremont_isl


isl_rpa_blueprint = Blueprint('isl_rpa_views', __name__, template_folder='templates')


@isl_rpa_blueprint.route('/isl-rpa', methods=['GET', 'POST'])
def isl_rpa():
    def generate_rpa(**kwargs):
        try:
            from_date = kwargs.get('query', {})
            fremont_isl(query)
        except Exception as e:
            print('System encountered an error running Fremont ISL RPA:\n')
            print_exc()
            email_body = 'System encountered an error running Fremont ISL RPA: %s' % e
            send_gmail('eanderson@khitconsulting.com', 'KHIT Report Notification', email_body)
                                
    if request.method == 'POST':
        query = request.form['from-date']
        thread = threading.Thread(target=generate_rpa, kwargs={'query': query})
        thread.start()
        return render_template('isl_rpa.html', title='ISL Automation', loading=True, from_date=query)
    return render_template('isl_rpa.html', title='ISL Automation')

