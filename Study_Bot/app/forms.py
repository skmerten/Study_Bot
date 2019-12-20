"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Question

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type', 'answer', 'incorrect_1', 'incorrect_2', 'incorrect_3']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)