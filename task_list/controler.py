from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Songs, Weather

bp = Blueprint('task_list', __name__)
app = Flask(__name__)

<<<<<<< HEAD

<<<<<<< HEAD
@bp.route('/', methods=('GET', 'POST'))
def index():
    
   return render_template('task_list/index.html')


=======
@app.route("/")
def welcome():
    return render_template(
        "index.html",
        test="wow this is crazy"
        )
>>>>>>> parent of d41ca91 (changes to Controler file)
=======
@bp.route('/')
def index():
   
    
    return render_template('task_list/index.html')
>>>>>>> parent of dbd90d3 (changing routes)
