from flask import Blueprint, render_template

fremont_blueprint = Blueprint('fremont_views', __name__, template_folder='templates')


@fremont_blueprint.route('/fremont')
def fremont():
    """ REST endpoint for the Fremont Webtools. """
    tools = {}
    return render_template('fremont.html', title='Fremont Webtools', tools=tools)
