import os
import feedparser
import requests
from dateutil import parser
from flask import Flask, render_template, redirect

from forms import PodcastNewForm


app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
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
        podcast_title = feed.channel.title
        podcast_image = feed.channel.image['href']
        podcast_summary = feed.channel.summary
        podcast_author = feed.channel.author

        for item in feed.entries:
            title = item.title
            link = item.link
            url = item['links'][1]['href']
            description = item.description
            pub_date=parser.parse(item.published)
        print("i", podcast_image, "t:", podcast_title, "l:", link, "u:", url, podcast_summary, "a:", podcast_author, description)
        return render_template('podcast_new.html', form=form, feed=feed)
    return render_template('podcast_submit.html', form=form)