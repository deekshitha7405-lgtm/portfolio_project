from django.shortcuts import render
from .models import Student, Project, Skill

def home(request):
    student = Student.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {'student': student, 'projects': projects, 'skills': skills})