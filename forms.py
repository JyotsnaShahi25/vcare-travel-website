"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    """Contact form."""
    query 	= TextAreaField("Query", [DataRequired()])
    submit  = SubmitField("Submit")
