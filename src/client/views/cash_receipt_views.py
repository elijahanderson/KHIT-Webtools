from flask import Blueprint, render_template, request, send_file
from werkzeug.utils import secure_filename
from xlrd import XLRDError

from client.forms.cash_receipt_form import CashReceiptForm
from infrastructure.cash_receipt import modify_cash_receipt

cash_receipt_blueprint = Blueprint('cash_receipt_views', __name__, template_folder='templates')


@cash_receipt_blueprint.route('/cash-receipt', methods=['GET', 'POST'])
def cash_receipt():
    """ REST endpoint for the cash receipt report interface. """
    form = CashReceiptForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(filename)
            try:
                modify_cash_receipt(filename)
                return render_template('cash_receipt.html', title='Cash Receipt', form=form, dl_file=filename)
            except KeyError as e:
                error_msg = 'The CSV file you selected does not contain the expected columns. Please ensure you selected the correct file and that it is a cash receipt report. ' \
                            'If this error persists, contact Eli at eanderson@khitconsulting.com'
                return render_template('cash_receipt.html', title='Cash Receipt', form=form, error_msg=error_msg)
            except XLRDError as e:
                error_msg = 'The XLS file you selected appears to be corrupted or has an outdated XLS format. Open it on your local machine and save it as an Excel 97-2003 Workbook ' \
                            ' (*.xls) and then retry uploading it. If that still doesn\'t work, try uploading it as a CSV file instead.'
                return render_template('cash_receipt.html', title='Cash Receipt', form=form, error_msg=error_msg)
            except Exception as e:
                error_msg = 'An unexpected error has occurred. If this error persists, contact Eli at eanderson@khitconsulting.com with this error message: ' + str(e)
                return render_template('cash_receipt.html', title='Cash Receipt', form=form, error_msg=error_msg)
    return render_template('cash_receipt.html', title='Cash Receipt', form=form)


@cash_receipt_blueprint.route('/cash-receipt-download/<dl_file>')
def cash_receipt_download(dl_file):
    return send_file('/client/client/' + dl_file, as_attachment=True)

