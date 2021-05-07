from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class NewPasteForm(FlaskForm):
    paste = StringField('Paste', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField()
