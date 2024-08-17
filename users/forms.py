import random
import string

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from mailing.forms import StyleFormMixin
from config.settings import EMAIL_HOST_USER
from users.models import User
from django.contrib.auth import password_validation


class UserRegForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

