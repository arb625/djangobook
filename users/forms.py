from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # required = true by default
    email = forms.EmailField()

    class Meta:
        # when form validates, it creates a new User
        model = User
        # fields to display on the form
        fields = ["username", "email", "password1", "password2"]

