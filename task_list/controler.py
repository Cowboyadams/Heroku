from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Songs, Weather

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Task name is required.')
        else:
            db.session.add(Songs(name=name))
            db.session.commit()

    tasks = Songs.query.all()
    return render_template('task_list/index.html', tasks=tasks)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    task = Songs.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('task_list.index'))
