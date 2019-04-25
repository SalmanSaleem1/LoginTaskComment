from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import TextAreaField, TextField, SubmitField


class NewPostForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired(), Length(min=5, max=50)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
