from django.shortcuts import render,redirect
# from .models import Post,Profiles,Answer,Category
from .models import Question,Invitation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from .email import send_welcome_email
from django.contrib.auth.models import User





# Create your views here.

def homePage(request):
    # categorys=Question.objects.get(category=cat)
    # posts=Question.objects.filter(category=categorys).count()
    posts=Question.objects.all().count()
    context={
        'posts':posts
    }
    return render(request,'homePage.html',context)


def signUp(request):
    currentUser=request.user
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')


            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password1 = form.cleaned_data['password1']
            # password2 = form.cleaned_data['password2']
            # user = User(username = username,email =email)
            # user.save()
            # useN=form.cleaned_data.get('username')
            send_welcome_email(username,email)
            # userN=form.cleaned_data.get('username')
            messages.success(request,f'{username} , your account was successfuly created')
            return redirect('logIn')
    else:
        form=UserRegistrationForm()
       
    return render(request,'auth/signUp.html',{'form':form})

def logIn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homePage')
    else:
        form=AuthenticationForm()
    return render(request,'auth/logIn.html',{'form':form})

def logOut(request):
    if request.method=='POST':
        logout(request)
    return redirect('logIn')
