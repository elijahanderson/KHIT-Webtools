from flask import Flask

from client.views.home_page import home_page
from client.views.aacog_views import aacog_blueprint
from client.views.ability_to_pay_views import ability_to_pay_blueprint
from client.views.cash_receipt_views import cash_receipt_blueprint
from client.views.fremont_views import fremont_blueprint

""" Initializes the app. """
app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(aacog_blueprint)
app.register_blueprint(ability_to_pay_blueprint)
app.register_blueprint(cash_receipt_blueprint)
app.register_blueprint(fremont_blueprint)
app.secret_key = "secret key"

