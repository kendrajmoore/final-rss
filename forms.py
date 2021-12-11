from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class PodcastNewForm(FlaskForm):
    podcast_url = StringField('Enter a RSS URL:')
    submit = SubmitField('Submit')
    
class SearchForm(FlaskForm):
    input_podcast = StringField('Enter Podcast Name: ')
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
class FeedForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    podcast_title = StringField('Podcast Title', validators=[DataRequired()])
    img = StringField('Podcast Logo', validators=[DataRequired()])
    homepage = StringField('Homepage', validators=[DataRequired()])
    podcast_title = StringField('Episode Title', validators=[DataRequired()])
    audio = StringField('Audio Link', validators=[DataRequired()])
    submit = SubmitField('Sign In')
