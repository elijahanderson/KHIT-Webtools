from flask import Flask, session

from client.views.home_page import home_page
from client.views.aacog_views import aacog_blueprint
from client.views.ability_to_pay_views import ability_to_pay_blueprint
from client.views.cash_receipt_views import cash_receipt_blueprint
from client.views.dpn_views import dpn_blueprint
from client.views.fremont_views import fremont_blueprint
from client.views.isl_rpa_views import isl_rpa_blueprint

""" Initializes the app. """
app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(aacog_blueprint)
app.register_blueprint(ability_to_pay_blueprint)
app.register_blueprint(cash_receipt_blueprint)
app.register_blueprint(dpn_blueprint)
app.register_blueprint(fremont_blueprint)
app.register_blueprint(isl_rpa_blueprint)
app.secret_key = "secret key"
app.config['REDIS_URL'] = 'redis://redis:6379/0'
app.config['QUEUES'] = ['default']


@app.before_first_request
def before_first_request():
    session['jobs'] = {}

