from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name = 'q_author')
    likes = models.ManyToManyField(User, related_name = 'q_likes')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, related_name ='a_author')
