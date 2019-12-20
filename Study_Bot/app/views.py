"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import QuestionForm
from app.models import Question
import random

def newQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # data processing
            return #Sometinf
    else:
        assert isinstance(request, HttpRequest)
        while True:
            select = random.randrange(1, Question.objects.all().count() + 1, 1)
            quest = Question.objects.get(id=select)
            if quest.number_correct < 2:
                break
        choices = [('correct', quest.correct_Ans ),('incorrect', quest.incorrect_1),('incorrect', quest.incorrect_2),('incorrect', quest.incorrect_3),]
        form = QuestionForm(initial={'question_text': quest.question_text, 'question_type': quest.question_type, 'number_correct': quest.number_correct}, answers = choices)
        return render(
            request,
            'app/newQuestion.html',
            {
                'title':'New Question',
                'year':datetime.now().year,
                'form':form
            }
        )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Score',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
