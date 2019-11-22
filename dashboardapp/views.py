from django.shortcuts import render,redirect
from django.db.models import Q
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Category,Answer,Profile
from .forms import NewQuestionForm,AnswerForm,ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url='/accounts/login/')
def page(request):
    categories = Category.objects.all()
    return render(request,'all-pages/index.html',{"categories": categories})

# @login_required(login_url='/accounts/login/')
def question_category(request, id):
    q_category = Category.objects.filter(id = id).first()
    questions = Question.objects.filter(category = q_category.id).all()
    return render(request,'question_category.html',{'q_category':q_category,"id":id,"questions":questions})

# @login_required(login_url='/accounts/login/')
def learn(request):
    post_question = Question.objects.all()
    return render(request,'all-pages/learn.html',{"post_question":post_question})  

# @login_required(login_url='/accounts/login/')
def question_answer(request, id):
    questions = Question.objects.filter(id = id).first()
    q_category = Category.objects.filter(id = questions.category.id).first() 
    answer = Answer.objects.filter(question = questions.id).all()
    related_question = Question.objects.filter(category = q_category.id).all()
    return render(request,'answers.html',{'q_category':q_category,"id":id,"questions":questions,"related_question":related_question,"answer":answer})

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

# @login_required(login_url='/accounts/login')
def post_answer(request, id):
    current_user = request.user
    question = Question.objects.filter(id=id).first()
    profiles = Profile.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = AnswerForm(request.POST,request.FILES)
        if form.is_valid():
            answers = form.save(commit=False)
            answers.user = current_user
            answers.question = question
            answers.save()
            return redirect('q_answer', id)
    else:
        form = AnswerForm()
    title = "Question"
    return render(request, 'add_answer.html',{"form":form, "id":id} )

# @login_required(login_url='/accounts/login/')
def new_profile(request):
  current_user = request.user
  new_profile = Profile.objects.filter(id=current_user.id)
  if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES)
      if form.is_valid():
          profile = form.save(commit=False)
          profile.username = current_user.profile
          profile.save()
      return redirect('profile')
  else:
      form = ProfileForm()
  return render(request, 'new-profile.html',{"form":form})

def profile(request):
    return render(request,'all-pages/profile.html',{})

# @login_required(login_url='/accounts/login/')
def profile(request):
 current_user = request.user
 myprofile = Profile.objects.filter(user = current_user).first()
 username = User.objects.filter(id = current_user.id).first()
 return render(request, 'profile.html', { "myprofile":myprofile})

# @login_required(login_url='/accounts/login/')
def search_question(request):
    if 'question' in request.GET and request.GET["question"]:
        search_term = request.GET.get("question")
        searched_question = Question.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, "search.html",{"message":message,"questions": searched_question})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})