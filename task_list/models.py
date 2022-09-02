import os
from sys import set_coroutine_origin_tracking_depth
from unicodedata import name
from task_list import db
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))

class Song(db.Model):
    __tablename__ = 'Songs'
    Song_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.VARCHAR(50))
    Artist = db.Column(db.VARCHAR(50))
    Genre = db.Column(db.VARCHAR(50))
    Spotify_api = db.Column(db.VARCHAR(250))
    Vibe = db.Column(db.Integer)

    def __init__(self,name,artist,genre,link,vibe):
        self.Name = name
        self.Artist = artist
        self.Genre = genre
        self.Spotify_api = link
        self.Vibe = vibe



    def __repr__(self):
        return f"the vibe is{name}"


def get_link():
    text = 'SELECT "spotify_api", "Vibe" FROM public."public.Song" Where "Vibe" = 2'
    return(text)