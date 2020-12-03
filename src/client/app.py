from flask import Flask

from src.client.views.home_page import home_page

""" Initializes the app. """
app = Flask(__name__)
app.register_blueprint(home_page)

