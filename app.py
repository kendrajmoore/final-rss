import os
basedir = os.path.abspath(os.path.dirname(__file__))
import re
import feedparser
import spacy
import requests
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
from flask_wtf.form import FlaskForm
from listennotes import podcast_api
from flask import Flask, render_template

from forms import PodcastNewForm, SearchForm, CreateForm
from dotenv import load_dotenv
load_dotenv()

KEY = os.environ.get("KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")



       
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        client = podcast_api.Client(api_key=KEY)
        searched_podcast = form.input_podcast.data
        response = client.search(q=searched_podcast, type='podcast')
        res_json = response.json()
        final_result = res_json['results']
        return render_template('results.html', form=form, final_result=final_result)   
    return render_template('search.html', form=form)

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        data = form.data
        response = json2xml.Json2xml(data, wrapper="all", pretty=True, attr_type=False).to_xml()
        return render_template('feed.html', form=form, response=response)   
    return render_template('create.html', form=form)

@app.route('/podcast', methods=['GET', 'POST'])
def podcastnew():
    form = PodcastNewForm()
    if form.validate_on_submit():
        url = form.podcast_url.data
        site = requests.get(url)
        with open('sitemap.xml', "w") as f:
            f.write(site.text)
        feed = feedparser.parse(url) 
        nlp = spacy.load('en_core_web_sm')
        if feed.channel.summary == None:
            return render_template('feed_error.html', title="Error"), 500
        else:
            description = feed.channel.summary
            results = nlp(description)
            keywords = results.ents
        for item in feed.entries:
            if item.description == None:
                return render_template('feed_error.html', title="Error"), 500
            else:
                #https://stackoverflow.com/questions/3398852/using-python-remove-html-tags-formatting-from-a-string/3398894     
                clean_regex = re.compile(r'<.*?>') 
        return render_template('podcast_new.html', form=form, feed=feed, clean_regex=clean_regex, keywords=keywords)
    return render_template('podcast_submit.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Error"), 404

@app.errorhandler(500)
def server_error(error):
    # note that we set the 404 status explicitly
    return render_template('error.html', title="Error"), 500