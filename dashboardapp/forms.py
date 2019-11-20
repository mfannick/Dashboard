from django import forms
from .models import Question
# from django.forms import ModelForm,Textarea,IntegerField

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user']
