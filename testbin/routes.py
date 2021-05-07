from flask import render_template, request, redirect, url_for, jsonify, make_response

from . import app, db
from .data import createPaste, getPaste
from .forms import NewPasteForm


@app.route('/', methods=['GET', 'POST'])
def index():
    paste_form = NewPasteForm()

    if paste_form.is_submitted():
        ID = createPaste(request.form['paste'])
        return redirect(url_for('raw_paste', ID=ID))
    else:
        return render_template(
            'index.html',
            paste_form=paste_form
        )


@app.route('/raw/<ID>', methods=['GET'])
def raw_paste(ID):
    response = make_response(getPaste(ID), 200)
    response.mimetype = 'text/plain'
    return response


@app.route('/all_pastes', methods=['GET'])
def all_pastes():
    return jsonify(db.pull('pastes'))
