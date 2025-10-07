from django.shortcuts import render,redirect
from .models import Project,Skill
from .forms import ContactForm

def index(request):
    tech_skills = Skill.objects.filter(category='tech', is_active=True).order_by('order', '-level')
    prof_skills = Skill.objects.filter(category='prof', is_active=True).order_by('order', '-level')
    projects = Project.objects.all()  # or filter(is_active=True)

    return render(request, 'index.html', {
        'tech_skills': tech_skills,
        'prof_skills': prof_skills,
        'projects': projects,
    })

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
    tech_skills = Skill.objects.filter(category=Skill.TECH, is_active=True)
    prof_skills = Skill.objects.filter(category=Skill.PROF, is_active=True)
    return render(request, "skills.html", {
        "tech_skills": tech_skills,
        "prof_skills": prof_skills,
    })