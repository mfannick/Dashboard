from django import forms
from .models import Question,Answer,Profile
# from django.forms import ModelForm,Textarea,IntegerField

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)
        widgets = {
            'answer': forms.Textarea(attrs={'cols': 30, 'rows': 3})
            }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user']