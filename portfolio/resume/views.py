from django.shortcuts import render,redirect
from .models import Project,Skill
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html',{'skills':skills, 'projects':projects})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def project(request):
    projects = Project.objects.all()
    return render(request,'projects.html',{'projects':projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'thankyou.html')
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})

def skills(request):
    skills= Skill.objects.all()
    return render(request,'skills.html',{'skills':skills})


def register_user(request):
    if request == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "registeration Successful")
            return redirect('index')
        else:
            messages.error(request, "please correct the error to register")
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


def login_user(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.info(request, f"Welcome back,{user.username}")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form= AuthenticationForm()
    return render(request,'login.html',{'form':form})