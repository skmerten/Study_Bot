"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Question
import random

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

class QuestionForm(ModelForm):
    possible_answers = forms.ChoiceField(label='Possible Answers')
    def __init__(self, answers, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question_text'].widget.attrs['readonly'] = True
        self.fields['possible_answers'].choices = answers
        self.fields['number_correct'].widget.attrs['readonly'] = True
        
    
    class Meta:
        model = Question
        fields = ['question_text', 'possible_answers', 'number_correct']
    
