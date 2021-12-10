import os
import re
import feedparser
import spacy
from flask_wtf.form import FlaskForm
from flask_moment import Moment
from listennotes import podcast_api
import requests
from dateutil import parser
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template, redirect

from forms import PodcastNewForm, SearchForm, LoginForm
from dotenv import load_dotenv
load_dotenv()

KEY = os.environ.get("KEY")

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
               

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        client = podcast_api.Client(api_key=KEY)
        searched_podcast = form.input_podcast.data
        response = client.search(q=searched_podcast)
        res_json = response.json()
        final_result = res_json['results']
        return render_template('results.html', form=form, final_result=final_result)   
    return render_template('search.html', form=form)

@app.route('/podcastnew', methods=['GET', 'POST'])
def podcastnew():
    form = PodcastNewForm()
    if form.validate_on_submit():
        url = form.podcast_url.data
        site = requests.get(url)
        with open('sitemap.xml', "w") as f:
            f.write(site.text)
        feed = feedparser.parse(url)
        for item in feed.entries:
            description = item.description
            nlp = spacy.load('en_core_web_sm')
            result = nlp(description)
            print(result.ents)
        
        return render_template('podcast_new.html', form=form, feed=feed)
    return render_template('podcast_submit.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Error"), 404

@app.errorhandler(500)
def server_error(error):
    # note that we set the 404 status explicitly
    return render_template('error.html', title="Error"), 500