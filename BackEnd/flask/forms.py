from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class ProjectEditFormFactory:
    @staticmethod
    def form(drinker, beers, bars):
        class F(FlaskForm):
            pid = Numeric(default=ProjectInfo.pid)
            name = StringField(default=ProjectInfo.name)
            num_spots = IntegerField(default=ProjectInfo.num_spots)





        return F()
