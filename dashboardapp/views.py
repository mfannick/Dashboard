from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Category,Answer,Profile
from .forms import NewQuestionForm,AnswerForm,ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/accounts/login/')

def page(request):
    categories = Category.objects.all()
    return render(request,'all-pages/index.html',{"categories": categories})

def question_category(request, id):
    q_category = Category.objects.filter(id = id).first()
    questions = Question.objects.filter(category = q_category.id).first()
    answer = Answer.objects.filter(question = questions.id).first()
    myanswers = Answer.objects.filter(question = answer.id).all()
    related_question = Question.objects.filter(category = q_category.id).all()
    return render(request,'all-pages/question_category.html',{'q_category':q_category,"id":id,"questions":questions,"related_question":related_question,"answer":answer,"myanswers":myanswers})


def learn(request):
    post_question = Question.objects.all()
    return render(request,'all-pages/learn.html',{"post_question":post_question})  

def question_answer(request, id):
    question = Question.objects.filter(id = id).first()
    myanswers = Answer.objects.filter(question = question.id).all()
    # q_category = Category.objects.filter(id = id).first()
    # questions = Question.objects.filter(category = q_category.id).first()
    # myanswers = Answer.objects.filter(question = questions.id).all()        
    return render(request,'all-pages/answers.html',{'question':question,"id":id, "myanswers":myanswers})


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
    return render(request, 'all-pages/post_question.html', {"form": form})

def home(request):
    current_user = request.user
    posts=Question.objects.all()
    solutions = Answer.objects.filter(id = current_user.id).first()
    return render(request,'all-pages/all.html',{'posts':posts,"solutions":solutions})

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
            return redirect('home')
    else:
        form = AnswerForm()
    title = "Question"
    return render(request, 'all-pages/add_answer.html',{"form":form, "id":id} )

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
  return render(request, 'all-pages/new-profile.html',{"form":form})

def profile(request):
    return render(request,'all-pages/profile.html',{})

def profile(request):
 current_user = request.user
 myprofile = Profile.objects.filter(user = current_user).first()
 username = User.objects.filter(id = current_user.id).first()
 return render(request, 'all-pages/profile.html', { "myprofile":myprofile})

def search_question(request):
    if 'question' in request.GET and request.GET["question"]:
        search_term = request.GET.get("question")
        searched_question = Question.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, "all-pages/search.html",{"message":message,"questions": searched_question})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pages/search.html',{"message":message})
def profile(request):
    return render(request,'all-pages/profile.html',{})  