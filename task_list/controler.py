from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Task

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
   
    return render_template('task_list/index.html')

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    task = Task.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('task_list.index'))