"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()
    question_type = models.TextField()
    answer = models.TextField()
    incorrect_1 = models.TextField()
    incorrect_2 = models.TextField()
    incorrect_3 = models.TextField()
    number_correct = models.IntegerField()


