import os
import re
import feedparser
from flask_wtf.form import FlaskForm
import requests
from dateutil import parser
from flask import Flask, render_template, redirect

from forms import PodcastNewForm, SearchForm


app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

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

@app.route("/search")
def search():
    form = SearchForm(FlaskForm)
    if form.validate_on_submit():
        url = form.input_podcast.data
        data = requests.get(url)
    return render_template('index.html')

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
        if feed.channel.title != None:
            podcast_title = feed.channel.title
        else:
            podcast_title = "No title"
        if feed.channel.image != None:
            podcast_image = feed.channel.image['href']
        else:
            podcast_image = None
        if feed.channel.summary is not None:
            podcast_summary = feed.channel.summary
        else:
            podcast_summary = "No summary available"
        if feed.channel.author is not None:   
            podcast_author = feed.channel.author
        for item in feed.entries:
            if item.title is not None:
                title = item.title
            else:
                title = "Not available"
            if item.link is not None:
                link = item.link
            else:
                link = "Not available"
            if item['links'][1]['href'] is not None:
               recording_url = item['links'][1]['href']
            else:
                recording_url = None
            if item.description is not None:
                description = item.description
                keywords = clean_text(description)
            else:
                description = "Not available"
            keywords = clean_text(description)
            if item.published is not None:
                pub_date=parser.parse(item.published)
            else:
                return None
        return render_template('podcast_new.html', form=form, feed=feed)
    return render_template('podcast_submit.html', form=form)