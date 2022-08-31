from task_list import db

class Songs(db.Model):
    song_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(50))
    artist = db.Column(db.VARCHAR(50))
    genre = db.Column(db.VARCHAR(50))
    song_vibe = db.Column(db.Integer)

    def __repr__(self):
        return '<Task: {}>'.format(self.name)

class Weather(db.Model):
    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    song_vibe = db.Column(db.Integer)

    def __repr__(self):
        return '<Task: {}>'.format(self.name)