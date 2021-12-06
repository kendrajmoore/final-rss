from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PodcastNewForm(FlaskForm):
    podcast_url = StringField('Enter a RSS URL:')
    submit = SubmitField('Submit')
    
class SearchForm(FlaskForm):
    input_podcast = StringField('Enter Podcast Name: ')
    submit = SubmitField('Submit')
