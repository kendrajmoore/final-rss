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
    
class CreateForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
