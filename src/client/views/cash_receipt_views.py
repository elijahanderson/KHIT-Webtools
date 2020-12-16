from flask import Blueprint, render_template, request
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
            form.file.data.save('src/uploads/' + filename)
            print('Upload success')
            return render_template('cash_receipt.html', title='Cash Receipt', form=form)
    return render_template('cash_receipt.html', title='Cash Receipt', form=form)
