from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jdm.models import Comment


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')

        