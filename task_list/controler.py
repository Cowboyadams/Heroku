from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
import requests
import pdb
from task_list import db

bp = Blueprint('task_list', __name__)



@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        form_data = request.form.get("zipcode")
        print(form_data)
        return render_template('index.html')
    
    if request.method == 'POST':
        #The users input (zipcode)
        user_zipcode = request.form['zipcode']
        print("\n the users zipcode is: \n" + user_zipcode + "\n")
        
        #Getting weather Data from Weather API
        weather_api = ('http://api.weatherapi.com/v1/forecast.json?key=6e399ba00ff24135ae584519223108&q=' + user_zipcode + '&days=1&aqi=no&alerts=no')
        weather_req = requests.get(weather_api)
        weather_res = weather_req.json()
        weather_res_text = weather_req.text
        print("the weather api results are: \n" + weather_res_text + "\n")

        return render_template(
            'index.html'
            )

