from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PodcastNewForm(FlaskForm):
    podcast_url = StringField('URL')
    submit = SubmitField('Submit')
