"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import QuestionForm
from app.models import Question, NumQuestions
import random
from django.shortcuts import redirect

def newQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['possible_answers']:
                question = Question.objects.get(question_text = form.cleaned_data['question_text'])
                question.number_correct = question.number_correct + 1
            
    else:
        assert isinstance(request, HttpRequest)
        number_of_ques = NumQuestions.objects.get(id = 1)
        number_of_ques = number_of_ques.number_questions
        question_set = []
        for x in range(number_of_ques):
            while True:
                select = random.randrange(1, Question.objects.all().count() + 1, 1)
                quest = Question.objects.get(id=select)
                if quest.number_correct < 2:
                    break
            choices = [(True, quest.correct_Ans ),(False, quest.incorrect_1),(False, quest.incorrect_2),(False, quest.incorrect_3),]
            random.shuffle(choices)
            form = QuestionForm(initial={'question_text': quest.question_text, 'number_correct': quest.number_correct}, answers = choices)
            question_set.append(form)
        return render(
            request,
            'app/newQuestion.html',
            {
                'title':quest.question_type,
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
