from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
#from task_list.models import Song

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        
        return render_template('index.html')
    else:
        return render_template('index.html')

