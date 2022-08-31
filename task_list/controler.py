from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Songs, Weather

bp = Blueprint('task_list', __name__)
app = Flask(__name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    
   return render_template('task_list/index.html')


