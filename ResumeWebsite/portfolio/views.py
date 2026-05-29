from django.shortcuts import render
from .models import Experience, Project, Skill


def home(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {'skills': skills})


def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {
        'experiences': experiences
    })


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {
        'projects': projects
    })


def contact(request):
    return render(request, 'portfolio/contact.html')