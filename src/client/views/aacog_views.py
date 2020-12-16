from flask import Blueprint, render_template

aacog_blueprint = Blueprint('aacog_views', __name__, template_folder='templates')

@aacog_blueprint.route('/aacog')
def aacog():
    """ REST endpoint for the AACOG Webtools. """
    tools = {
        'Ability To Pay Calculator': '/ability-to-pay'
    }
    return render_template('aacog.html', title='AACOG Webtools', tools=tools)
