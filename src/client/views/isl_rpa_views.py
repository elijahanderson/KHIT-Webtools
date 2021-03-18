import json
import os
import redis

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
        with Connection(redis.from_url(current_app.config['REDIS_URL'])):
            q = Queue()
            c_job_id = generate_id(20)
            job = q.enqueue(fremont_isl, from_date, c_job_id, job_id=c_job_id, result_ttl=86400)
            jobs = session['jobs']
            jobs[c_job_id] = {'from_date': from_date, 'status': job.get_status(), 'result': ''}
            session['jobs'] = jobs
        return redirect(url_for('isl_rpa_views.isl_jobs'))
    return render_template('isl_rpa.html', title='ISL Automation')


@isl_rpa_blueprint.route('/isl-rpa/jobs', methods=['GET'])
def isl_jobs():
    """ REST endpoint for viewing RQ statuses. """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        jobs = session['jobs']
        for job_id in jobs.keys():
            job = q.fetch_job(job_id)
            if job is None:
                jobs.pop(job_id, None)
            else:
                jobs[job_id]['status'] = job.get_status()
                jobs[job_id]['result'] = job.result if job.result is not None else ''
            # TODO -- if job has failed, give user option to retry or delete it
        session['jobs'] = jobs
        sorted_jobs = sorted(jobs.items(), key=lambda job: job['from_date'])
        return render_template('jobs.html', title='ISL Automation', jobs=sorted_jobs)


@isl_rpa_blueprint.route('/isl-rpa/retry-job-<job_id>', methods=['GET'])
def retry_job(job_id):
    """ REST endpoint for retrying a job. """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        jobs = session['jobs']
        from_date = jobs[job_id]['from_date']
        job = q.enqueue(fremont_isl, from_date, job_id, job_id=job_id, result_ttl=86400)
        jobs[job_id]['status'] = job.get_status()
        jobs[job_id]['result'] = job.result if job.result is not None else ''
        session['jobs'] = jobs
        return redirect(url_for('isl_rpa_views.isl_jobs'))
