from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        form_data = request.form.get("zipcode")
        print(form_data)
        return render_template('index.html')
    
    if request.method == 'POST':
        user_zipcode = request.form['zipcode']
        print(user_zipcode)
        return render_template('index.html', user_zipcode=user_zipcode)

