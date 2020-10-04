# Using wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('Title required')])
    content = TextAreaField('내용', validators=[DataRequired('Content Required')])



class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators = [DataRequired('Content Required')])