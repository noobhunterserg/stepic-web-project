from django import forms
from .models import Question, Answer

class Add_Question(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text',)

class Add_Answer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)
