import os
import re
import feedparser
from flask_wtf.form import FlaskForm
from flask_moment import Moment
import requests
from dateutil import parser
from config import Config
from flask import Flask, render_template, redirect

from forms import PodcastNewForm, SearchForm


app = Flask(__name__)
app.config.from_object(Config)

def clean_text(text):
    wordcount = {}
    text = text.lower()
    # text_no_punc = re.sub(r'[^\w\s]','',text)
    # stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    # for line in text_no_punc:
    #     if line not in stopwords:
    #         if line not in wordcount:
    #             wordcount[line] = 1
    #         else:
    #             wordcount[line] += 1
    #print(text)
               

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        searched_podcast = form.input_podcast.data
        headers = {
        'X-ListenAPI-Key': '492e2d30fd1144f6a640da16d650c2c1',
        }
        response = requests.request('GET', url, headers=headers)
        return render_template('results.html', form=form)   
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
        #print(feed)
        return render_template('podcast_new.html', form=form, feed=feed)
    return render_template('podcast_submit.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Error")

@app.errorhandler(500)
def server_error(error):
    # note that we set the 404 status explicitly
    return render_template('error.html', title="Error")