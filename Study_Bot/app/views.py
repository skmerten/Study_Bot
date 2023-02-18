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
        question = Question.objects.get(question_text = request.POST.get('question_text'))
        if request.POST.get('possible_answers') == 'True':
            question.number_correct = question.number_correct + 1
            question.save()
            return render(
                request,
                'app/correct.html',
                {
                    'title': 'Correct',
                    'year':datetime.now().year
                }
            )
        else:
            question.number_correct = 0
            question.save()
            return render(
                request,
                'app/wrong.html',
                {
                    'title': 'Incorrect',
                    'question': question.question_text,
                    'correct_answer': question.correct_Ans,
                    'year':datetime.now().year
                }
            )

    else:
        assert isinstance(request, HttpRequest)
        number_of_ques = NumQuestions.objects.get(id = 1)
        number_of_ques = number_of_ques.number_questions

        number_cor = NumQuestions.objects.get(id = 2)
        number_cor = number_cor.number_questions

        question_set = []
        selected_ids = []

        allQuestions = Question.objects.all()
        questionsCompleted = True

        for question in allQuestions:
            if question.number_correct < number_cor:
                questionsCompleted = False
                break
        
        if questionsCompleted == True:
            questions = Question.objects.all()
            scores = []
            for each in questions:
                scores.append(each.number_correct)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/score.html',
                {
                    'title':'You are all done! Reset to continue.',
                    'complete':scores.count(2),
                    'partial':scores.count(1),
                    'incomplete':scores.count(0),
                    'complete_perc':round(scores.count(2) / len(scores), 2)*100,
                    'partial_perc':round(scores.count(1) / len(scores), 2)*100,
                    'incomplete_perc':round(scores.count(0) / len(scores), 2)*100,
                    'year':datetime.now().year,
                    'complete': True,
                }
            )
        else:
            for x in range(number_of_ques):
                while True:
                    select = random.randrange(1, Question.objects.all().count() + 1, 1)
                    quest = Question.objects.get(id=select)
                    if quest.number_correct < number_cor:
                        if not select in selected_ids:
                            selected_ids.append(select)
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
                    'forms':question_set,
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

def settings(request):
    if request.method == 'POST':
        if request.POST.get('reset') == 'Reset':
            questions = Question.objects.all()
            for each in questions:
                each.number_correct = 0
                each.save()
        if not request.POST.get('questionNum') == '':
            numQs = NumQuestions.objects.get(id=1)
            numQs.number_questions = request.POST.get('questionNum')
            numQs.save()
        if not request.POST.get('numberCorrect') == '':
            numCorrect = NumQuestions.objects.get(id=2)
            numCorrect.number_questions = request.POST.get('numberCorrect')
            numCorrect.save()
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/settings.html',
            {
                'title':'Settings',
                'year':datetime.now().year,
            }
        )
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/settings.html',
            {
                'title':'Settings',
                'year':datetime.now().year,
            }
        )

def score(request):
    questions = Question.objects.all()
    numCorrect = NumQuestions.objects.get(id=2)
    scores = []
    for each in questions:
        scores.append(each.number_correct)
    partialComplete = len(questions) - (scores.count(numCorrect.number_questions) + scores.count(0))
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/score.html',
        {
            'title':'Score',
            'complete':scores.count(numCorrect.number_questions),
            'partial': partialComplete,
            'incomplete':scores.count(0),
            'complete_perc':round(scores.count(numCorrect.number_questions) / len(scores), 2)*100,
            'partial_perc':round(partialComplete / len(scores), 2)*100,
            'incomplete_perc':round(scores.count(0) / len(scores), 2)*100,
            'year':datetime.now().year,
        }
    )
