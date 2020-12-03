from flask import Blueprint, render_template, session

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/', defaults={'page': 'home'})
@home_page.route('/home', defaults={'page': 'home'})
def home(page):
    """ REST endpoint for the home dashboard. """
    return render_template('home.html', title='Home')
