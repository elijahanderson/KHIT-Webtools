from flask import Blueprint, render_template

fremont_blueprint = Blueprint('fremont_views', __name__, template_folder='templates')


@fremont_blueprint.route('/fremont')
def fremont():
    """ REST endpoint for the Fremont Webtools. """
    tools = {
        'Cash Receipt Report': '/cash-receipt',
        'ISL Automation': '/isl-rpa',
        'DPN Report': '/dpn'
    }
    return render_template('fremont.html', title='Fremont Webtools', tools=tools)
