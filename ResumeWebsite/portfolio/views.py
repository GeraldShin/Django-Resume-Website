from django.shortcuts import render
from .models import Experience, Project, Skill, Profile


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()

    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'skills': skills
    })

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

