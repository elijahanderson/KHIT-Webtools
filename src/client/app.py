from flask import Flask

from src.client.views.home_page import home_page
from src.client.views.aacog_views import aacog_blueprint
from src.client.views.ability_to_pay_views import ability_to_pay_blueprint
from src.client.views.cash_receipt_views import cash_receipt_blueprint
from src.client.views.dpn_views import dpn_blueprint
from src.client.views.fremont_views import fremont_blueprint
from src.client.views.isl_rpa_views import isl_rpa_blueprint

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
