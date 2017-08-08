from django import forms
from .models import Question

class Add_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text',)
    # title = forms.CharField(100)
    # text  = forms.CharField(widget=forms.Textarea)
