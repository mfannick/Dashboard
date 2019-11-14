from django.shortcuts import render,redirect
# from .models import Post,Profiles,Answer,Category

# Create your views here.

def homePage(request):
    # posts=Post.objects.all()
    # context={
    #     'posts':posts
    # }
    return render(request,'homePage.html')
