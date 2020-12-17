import pandas as pd

from flask import Blueprint, render_template, request, send_file
from werkzeug.utils import secure_filename

from client.forms.cash_receipt_form import CashReceiptForm

cash_receipt_blueprint = Blueprint('cash_receipt_views', __name__, template_folder='templates')


@cash_receipt_blueprint.route('/cash-receipt', methods=['GET', 'POST'])
def cash_receipt():
    """ REST endpoint for the cash receipt report interface. """
    form = CashReceiptForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(filename)
            df = pd.read_csv(filename)
            df = df[['payor_name', 'check_no', 'check_date', 'deposit_number']]
            df['check_date'] = pd.to_datetime(df.check_date)
            df.sort_values(by=['check_date'], inplace=True)
            df.to_csv('/client/client/' + filename, index=False)
            return render_template('cash_receipt.html', title='Cash Receipt', form=form, dl_file=filename)
    return render_template('cash_receipt.html', title='Cash Receipt', form=form)

@cash_receipt_blueprint.route('/cash-receipt-download/<dl_file>')
def cash_receipt_download(dl_file):
    return send_file('/client/client/' + dl_file, as_attachment=True)

