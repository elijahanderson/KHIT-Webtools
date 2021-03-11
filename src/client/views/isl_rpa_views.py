import redis

from flask import Blueprint, current_app, redirect, render_template, request, url_for
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
            job = q.enqueue(fremont_isl, from_date)
            job.meta['from_date'] = from_date
            job.save_meta()
        return redirect(url_for('isl_rpa_views.isl_jobs'))
    return render_template('isl_rpa.html', title='ISL Automation')


@isl_rpa_blueprint.route('/isl-rpa/jobs', methods=['GET'])
def isl_jobs():
    """ REST endpoint for viewing RQ statuses. """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        jobs = q.jobs
        for job in jobs:
            print(job.get_status())
        return render_template('jobs.html', title='ISL Automation', jobs=jobs)

