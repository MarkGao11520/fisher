"""
create by gaowenfeng on 
"""
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.user import User

__author__ = "gaowenfeng"


class RegisterForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64, message='电子邮箱不符合规范')])

    nickname = StringField('昵称', validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64, message='电子邮箱不符合规范')])

    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])

