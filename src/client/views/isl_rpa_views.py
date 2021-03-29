import os
import pandas as pd
import redis

from datetime import timedelta
from flask import Blueprint, current_app, redirect, render_template, request, session, url_for
from rq import Queue, Connection

from infrastructure.email import send_gmail
from infrastructure.helpers import generate_id
from infrastructure.isl_rpa import fremont_isl

isl_rpa_blueprint = Blueprint('isl_rpa_views', __name__, template_folder='templates')


@isl_rpa_blueprint.route('/isl-rpa', methods=['GET', 'POST'])
def isl_rpa():
    """ REST endpoint to handle generating ISLs. """
    if request.method == 'POST':
        from_date = request.form['from-date']
        to_date = request.form['to-date']
        if session.get('jobs'):
            session['jobs'] = enqueue_date_range(from_date, to_date, session['jobs'])
            session.modified = True
        else:
            session['jobs'] = enqueue_date_range(from_date, to_date, {})
            session.modified = True
        print(session['jobs'])
        return redirect(url_for('isl_rpa_views.isl_jobs'))
    return render_template('isl_rpa.html', title='ISL Automation')


@isl_rpa_blueprint.route('/isl-rpa/jobs', methods=['GET'])
def isl_jobs():
    """ REST endpoint for viewing RQ statuses. """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        print(q.jobs)
        print(q.job_ids)
        jobs = session['jobs']
        njobs = {}
        for job_id in jobs.keys():
            job = q.fetch_job(job_id)
            if job is None:
                print(f"{job_id} not found; removing from queue.")
            else:
                result = job.result if job.result is not None and job.result is not ''  else ''
                njobs[job_id] = [jobs[job_id][0], job.get_status(), result]

        session['jobs'] = njobs
        session.modified = True
        print(session['jobs'])
        df = pd.DataFrame.from_dict(njobs, orient='index', columns=['from_date', 'status', 'result'])
        print(df)
        sorted_jobs = df.sort_values(by=['from_date', 'status', 'result']).to_dict('index')
    return render_template('jobs.html', title='ISL Automation', jobs=sorted_jobs)


@isl_rpa_blueprint.route('/isl-rpa/retry-job-<job_id>', methods=['GET'])
def retry_job(job_id):
    """ REST endpoint for retrying a job. """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        jobs = session['jobs']
        from_date = jobs[job_id][0]
        jobs.pop(job_id, None)
        session['jobs'] = enqueue_date_range(from_date, '', jobs)
        session.modified = True
    return redirect(url_for('isl_rpa_views.isl_jobs'))



#@isl_rpa_blueprint.route('/isl-rpa/cancel-job-<job_id>', methods=['GET'])
#def cancel_job(job_id):
#    """ REST endpoint for cancelling a job. """
#    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
#        q = Queue()
#        job = q.fetch_job(job_id)
#        job.cancel()
#        print(f"Cancelling {job_id}") 
#    return redirect(url_for('isl_rpa_views.isl_jobs'))


def enqueue_date_range(from_date, to_date, jobs):
    """ Main queue handler. """
    from_date = pd.to_datetime(from_date)
    day_diff = (abs((pd.to_datetime(to_date) - from_date).days) + 1) if to_date != '' else False
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        if not day_diff:
            job_id = generate_id(20)
            job = q.enqueue(fremont_isl, from_date, job_id=job_id, result_ttl=86400)
            jobs[job_id] = [from_date.strftime('%Y-%m-%d'), job.get_status(), '']
        else:
            for fdate in (from_date + timedelta(days=n) for n in range(day_diff)):
                job_id = generate_id(20)
                job = q.enqueue(fremont_isl, fdate, job_id=job_id, result_ttl=86400)
                jobs[job_id] = [fdate.strftime('%Y-%m-%d'), job.get_status(), '']
    return jobs

