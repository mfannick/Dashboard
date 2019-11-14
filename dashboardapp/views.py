from django.shortcuts import render,redirect
# from .models import Post,Profiles,Answer,Category
from .models import Question


# Create your views here.

def homePage(request):
    # categorys=Question.objects.get(category=cat)
    # posts=Question.objects.filter(category=categorys).count()
    posts=Question.objects.all().count()
    context={
        'posts':posts
    }
    return render(request,'homePage.html',context)
