from mailing.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from users.models import User
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)
