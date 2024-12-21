from django.db import models


class Question(models.Model):
    question_number = models.CharField(max_length=3)
    question_text = models.CharField(max_length=255)
    question_autor = models.CharField(max_length=30)



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_char = models.CharField(max_length=1)
    answer_text = models.CharField(max_length=255)
    user_choice = models.IntegerField(default=0)
