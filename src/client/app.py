from flask import Flask

from client.views.home_page import home_page
from client.views.ability_to_pay_views import ability_to_pay_blueprint

""" Initializes the app. """
app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(ability_to_pay_blueprint)
app.secret_key = "secret key"
