from flask import Blueprint, redirect, render_template, request,  url_for
import json
from os import remove
from werkzeug.utils import secure_filename
from xlrd import XLRDError

from client.forms.dpn_form import DPNForm
from infrastructure.dpn import modify_dpn

dpn_blueprint = Blueprint('dpn_views', __name__, template_folder='templates')


@dpn_blueprint.route('/dpn', methods=['GET', 'POST'])
def dpn():
    """ REST endpoint for the cash receipt report interface. """
    form = DPNForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(filename)
            try:
                output = modify_dpn(filename)
                print(output)
                remove(filename)
                with open('json/output.json', 'w') as outfile:
                    json.dump(output, outfile)
                return redirect(url_for('dpn_views.display_categories', page_no=1))
            except KeyError as e:
                error_msg = 'The CSV file you selected does not contain the expected columns. ' \
                            'Please ensure you selected' \
                            ' the correct file and that it is a DPN report. ' \
                            'If this error persists, contact Eli at eanderson@khitconsulting.com'
                return render_template('dpn.html', title='Cash Receipt', form=form, error_msg=error_msg)
            except XLRDError as e:
                error_msg = 'The XLS file you selected appears to be corrupted or has an outdated XLS format. ' \
                            'Open it on your local machine and save it as an Excel 97-2003 Workbook ' \
                            ' (*.xls) and then retry uploading it. If that still doesn\'t work, try uploading it as a '\
                            'CSV file instead.'
                return render_template('dpn.html', title='Cash Receipt', form=form, error_msg=error_msg)
            except Exception as e:
                error_msg = 'An unexpected error has occurred. If this error persists, contact Eli at ' \
                            'eanderson@khitconsulting.com with this error message: ' + str(e)
                return render_template('dpn.html', title='Cash Receipt', form=form, error_msg=error_msg)
    return render_template('dpn.html', title='Cash Receipt', form=form)


@dpn_blueprint.route('/dpn/<page_no>', methods=['GET', 'POST'])
def display_categories(page_no):
    form = DPNForm()
    page_no = int(page_no)
    with open('json/output.json') as output_file:
        output = json.load(output_file)
    output_split = {}
    pg = 1
    pages = []
    for i in range(0, len(output.items()), 27):
        pages.append(pg)
        for item in list(output.items())[i:i+27]:
            if pg in output_split.keys():
                output_split[pg].append(item)
            else:
                output_split[pg] = [item]
        pg = pg + 1
    try:
        return render_template('display_categories.html', title='Cash Receipt', form=form, output=output_split[page_no],
                               page_no=page_no, pages=pages)
    except Exception as e:
        error_msg = 'An unexpected error has occurred. If this error persists, contact Eli at ' \
                    'eanderson@khitconsulting.com with this error message: ' + str(e)
        return render_template('dpn.html', title='Cash Receipt', form=form, error_msg=error_msg)
