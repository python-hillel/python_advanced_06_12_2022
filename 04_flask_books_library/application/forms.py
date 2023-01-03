from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class CreateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = StringField(label='Author', validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField(label='Create')


class DeleteBookForm(FlaskForm):
    submit = SubmitField(label='Delete')


class UpdateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = StringField(label='Author', validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField(label='Update')
