"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def newQuestion(request):
    """Renders a new question page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newQuestion.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
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

def score(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/score.html',
        {
            'title':'Score',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
