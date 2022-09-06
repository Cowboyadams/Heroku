from os import curdir
import os
from re import S
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask import Flask
import requests
from task_list import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
import psycopg2
from .models import Song
from .vibecheck import vibecheck
bp = Blueprint('task_list', __name__)
app = Flask(__name__)
sql = SQLAlchemy(app)



@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        form_data = request.form.get("zipcode")
        print(form_data)
        return render_template('index.html')
    
    if request.method == 'POST':

#       The users input (zipcode) ----------------------------------------------------------------------------------------------------------------------------

        user_zipcode = request.form['zipcode']
        print("\n the users zipcode is: \n" + user_zipcode + "\n")
        
#       Getting weather Data from Weather API ----------------------------------------------------------------------------------------------------------------

        weather_api = ('http://api.weatherapi.com/v1/forecast.json?key=6e399ba00ff24135ae584519223108&q=' + user_zipcode + '&days=1&aqi=no&alerts=no')
        weather_req = requests.get(weather_api)
        weather_res = weather_req.json()
        weather_res_text = weather_req.text
        print("the weather api results are: \n" + weather_res_text + "\n")

#       Declaring Variables -----------------------------------------------------------------------------------------------------------------------------------

        user_local = weather_res["location"]["name"]
        user_date = weather_res["location"]["localtime"]
        is_day = weather_res["current"]["is_day"]
        cloud_percent = weather_res["current"]["cloud"]
        rain = weather_res["current"]["precip_in"]
        uv = weather_res["current"]["uv"]
        info = [user_local, user_date, is_day, cloud_percent, rain, uv]

#       Vibecheck ---------------------------------------------------------------------------------------------------------------------------------------------
        print(info)
        print(info[4])
        print(type(info[4]))
        vibe_num = vibecheck(info)
        
        
#       Getting Database info
        result = Song.query.filter(Song.Vibe==vibe_num).first()

#       Making reference string
        
        string_result = result.Spotify_api
        
        print(string_result)
        
        ref = string_result
        
        return render_template(
            'songs.html',
          
#           Variables used in HTML Template
            user_local=user_local, 
            is_day=is_day,
            cloud_percent=cloud_percent,
            rain=rain,
            user_date=user_date,
            ref=ref
            )

