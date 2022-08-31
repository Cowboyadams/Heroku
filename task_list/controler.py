from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Songs

bp = Blueprint('task_list', __name__)


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "index.html",
        test="wow this is crazy"
        )
