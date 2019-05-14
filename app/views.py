from flask_wtf import FlaskForm
from flask import render_template, flash, redirect, session, url_for, request
from wtforms import Field, Label, SubmitField, StringField, validators, ValidationError
from app import app, db, admin
from app.models import User, Video

# Views
@app.route('/')
@app.route('/index')
def home():

    form = FlaskForm()
    return render_template('index.html',\
            title='Anime Search',\
            videos=Video.query.all())
