from django.shortcuts import render
from .models import Experience, Project, Skill

def home(request):
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    skills = Skill.objects.all()

    return render(
        request,
        "portfolio/home.html",
        {
            "experiences": experiences,
            "projects": projects,
            "skills": skills,
        }
    )