from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UploadForm(forms.Form):
    households = forms.FileField(required=False)
    products = forms.FileField(required=False)
    transactions = forms.FileField(required=False)
