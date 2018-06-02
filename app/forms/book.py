"""
create by gaowenfeng on 
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = "gaowenfeng"


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message="查询关键字长度必须在1-30之间")], )
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
