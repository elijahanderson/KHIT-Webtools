import redis

from flask import Blueprint, current_app, redirect, render_template, request
from rq import Queue, Connection

from infrastructure.email import send_gmail
from infrastructure.isl_rpa import fremont_isl


isl_rpa_blueprint = Blueprint('isl_rpa_views', __name__, template_folder='templates')


@isl_rpa_blueprint.route('/isl-rpa', methods=['GET', 'POST'])
def isl_rpa():
    """ REST endpoint to handle generating ISLs. """
    if request.method == 'POST':
        from_date = request.form['from-date']
        with Connection(redis.from_url(current_app.config['REDIS_URL'])):
            q = Queue()
            task = q.enqueue(fremont_isl, from_date)
        return render_template('isl_rpa.html', title='ISL Automation', loading=True, from_date=from_date)
    return render_template('isl_rpa.html', title='ISL Automation')

