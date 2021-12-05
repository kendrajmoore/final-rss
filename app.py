import os
import re
import feedparser
import requests
from dateutil import parser
from flask import Flask, render_template, redirect

from forms import PodcastNewForm


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
    print(text)
        
        

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
            recording_url = item['links'][1]['href']
            description = item.description
            keywords = clean_text(description)
            
            pub_date=parser.parse(item.published)
        print("i", podcast_image, "t:", podcast_title, "l:", link, "u:", url, podcast_summary, "a:", podcast_author, description)
        return render_template('podcast_new.html', form=form, feed=feed)
    return render_template('podcast_submit.html', form=form)