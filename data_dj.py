import random
from ask.qa.models import Question, Answer

for i in range(1, 100):
    title = 'title' + str(i)
    text = 'text' + str(i)
    q = Question.objects.create(title=title, text=text)
    q.save()
    for k in range (5):
        comment = 'comment' + str(i)
        a = Answer.objects.create(text=comment)
        a.save()
