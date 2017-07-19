from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete = models.SET_NULL)
    likes = models.ManyToMany(User, related_name = 'q_likes')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(User, on_delete = models.SET_NULL)
    author = models.ForeignKey(User, on_delete = models.SET_NULL)
