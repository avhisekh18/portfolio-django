from django.shortcuts import render,redirect
from .models import Project,Skill
from .forms import ContactForm

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


