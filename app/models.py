from app import app, db, admin
from flask_admin.contrib.sqla import ModelView

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

class Video(db.Model):
    __tablename='video'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False)
    genre = db.Column(db.String(50), unique=False)
    season = db.Column(db.Integer, unique=False)
    episode = db.Column(db.Integer, unique=False)
    description = db.Column(db.String(250), unique=False)
    
    def __repr__(self):
        return "{Title: %r,\nGenre: %r,\nSeason: %r,\nEpisode: %r,\nDescription: %r}\n" % (self.title,self.genre,self.season,self.episode,self.description)

    def save(self):
        db.session.add(self)
        db.session.commit()        

class UserView(ModelView):
    def __init__(self,session,**kwargs):
        super(UserView,self).__init__(User,session,**kwargs)

class VideoView(ModelView):
    def __init__(self,session,**kwargs):
        super(VideoView,self).__init__(Video,session,**kwargs)

admin.add_view(UserView(db.session))
admin.add_view(VideoView(db.session))
