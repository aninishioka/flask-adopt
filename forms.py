"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, URLField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name",
                       validators=[InputRequired()])

    species = StringField("Pet Species",
                          validators=[InputRequired()])

    photo_url = URLField("Pet Photo URL",
                         validators=[Optional(), URL()])

    age = SelectField("Pet Age",
                      choices=[("baby", "Baby"), ("young", "Young"),
                               ("adult", "Adult"), ("senior", "Senior")])

    notes = StringField("Pet Notes")

    available = BooleanField("Pet Availability",
                             validators=[InputRequired()],
                             coerce=bool)

