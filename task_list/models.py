import os
from sys import set_coroutine_origin_tracking_depth
from unicodedata import name
#from task_list import db
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

    def __repr__(self) -> str:
        return f"{self.Spotify_api}"

    




def get_link():
    text = 'SELECT "spotify_api", "Vibe" FROM public."public.Song" Where "Vibe" = 2'
    return(text)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lbyxwmuqvbndrv:948908345954624da81b9a539c830d5122aff868c7f927efc3ce5e5a2bf31350@ec2-44-205-63-142.compute-1.amazonaws.com:5432/df6ube44s5bk3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    
    def load_songs():
        print("Song")
        Song.query.delete()
        for row in open("static\songs.item"):
            row = row.rstrip()
            name, artist, genre, link, vibe = row.split("|")

            list = Song(name=name,
                        artist=artist,
                        genre=genre,
                        link=link,
                        vibe=vibe)
            db.session.add(list)
        db.session.commit()
    
    load_songs()
    print("Connected to database")