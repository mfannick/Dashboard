from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Category
from .forms import NewQuestionForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/accounts/login/')
def homePage(request):
  
    categories = Category.objects.all()
    return render(request,'homePage.html',{"categories": categories})

def question_category(request, id):
    q_category = Category.objects.filter(id = id).first()
    questions = Question.objects.filter(category = q_category.id).first()
    related_question = Question.objects.filter(category = q_category.id).all()
    return render(request,'question_category.html',{'q_category':q_category,"id":id, "questions":questions,"related_question":related_question})

def questions(request):
    posts = Question.objects.all()
    context={
        'posts':posts
    }
    return render(request,'question.html',context)


# @login_required(login_url='/accounts/login/')
def post_question(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = NewQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('question')

    else:
        form = NewQuestionForm()
    return render(request, 'post_question.html', {"form": form})

def search_question(request):
    if 'question' in request.GET and request.GET["question"]:
        search_term = request.GET.get("question")
        searched_question = Question.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, "search.html",{"message":message,"questions": searched_question})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
