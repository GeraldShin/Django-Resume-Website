from django.shortcuts import render
from django.conf import settings
import json
from pathlib import Path
from .models import Experience, Project, Skill

def home(request):
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    skills = Skill.objects.all()

    data_path = Path(settings.BASE_DIR) / "portfolio" / "data" / "resume_data.json"
    with open(data_path, "r", encoding="utf-8") as file:
        resume = json.load(file)

    return render(
        request,
        "portfolio/home.html",
        resume,
        # { # we dont use this anymore since we're going to skip CloudSQL cost
        #     "experiences": experiences,
        #     "projects": projects,
        #     "skills": skills,
        # }
    )