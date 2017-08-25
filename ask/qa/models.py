from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

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

    def get_url(self):
        return reverse('question_page',
                        kwargs={'num': self.id}
                        )

    def __str__(self):
        return self.title

    def time_since_created(self):
        return (timezone.now()-self.added_at).seconds//60

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, related_name ='a_author')
