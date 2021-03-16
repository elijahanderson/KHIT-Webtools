import json
import redis

from flask import Blueprint, current_app, redirect, render_template, request, url_for
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
            job_id = generate_id(20)
            job = q.enqueue(fremont_isl, from_date, job_id, job_id=job_id, result_ttl=86400)
            #job.meta['from_date'] = from_date
            #job.save_meta()0
            job_id = job.get_id()
            jobfile = open('json/jobs.json', 'r')
            jobs = json.load(jobfile)
            print(jobs)
            jobs[job_id] = {'from_date': from_date}
            jobfile.close()
            jobfile = open('json/jobs.json', 'w')
            json.dump(jobs, jobfile)
            jobfile.close()

        return redirect(url_for('isl_rpa_views.isl_jobs'))
    return render_template('isl_rpa.html', title='ISL Automation')


@isl_rpa_blueprint.route('/isl-rpa/jobs', methods=['GET'])
def isl_jobs():
    """ REST endpoint for viewing RQ statuses. """
    with Connection(redis.from_url(current_app.config['REDIS_URL'])):
        q = Queue()
        jobfile = open('json/jobs.json', 'r')
        jobs = json.load(jobfile)
        for job_id in jobs.keys():
            job = q.fetch_job(job_id)
            if job is None:
                jobs.pop(job_id, None)
            # TODO -- if job has failed, give user option to retry or delete it
        jobfile.close()
        jobfile = open('json/jobs.json', 'w')
        json.dump(jobs, jobfile)
        jobfile.close()
        print(jobs)
        return render_template('jobs.html', title='ISL Automation', jobs=jobs)

