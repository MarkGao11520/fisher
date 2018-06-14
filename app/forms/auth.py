"""
create by gaowenfeng on 
"""
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo

from app.models.user import User

__author__ = "gaowenfeng"


class EmailForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64, message='电子邮箱不符合规范')])


class RegisterForm(EmailForm):
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


class LoginForm(EmailForm):
    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])


class ResetPasswordForm(Form):
    password1 = PasswordField('新密码', validators=[
        DataRequired(), Length(6, 20, message='密码长度至少需要在6到20个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField('确认新密码', validators=[
        DataRequired(), Length(6, 20)])



