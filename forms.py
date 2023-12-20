from wtforms import StringField, IntegerField, TimeField, SubmitField,DateField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf import FlaskForm

class BookingForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    num_people = IntegerField('Number of Guests', validators=[NumberRange(min=0, max=20),DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"type": "date"})
    time = TimeField('Time', format='%H:%M', validators=[DataRequired()], render_kw={"type": "time"})
    submit = SubmitField('Book Table')
