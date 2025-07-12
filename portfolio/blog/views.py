from django.shortcuts import render
from .models import Project, BlogPost, Skill, AdditionalSkill

def home(request):
    skills = Skill.objects.all()
    additional_skills = AdditionalSkill.objects.all()
    projects = Project.objects.all().order_by('-created_at')[:3]  # hanya 3 project terbaru
    blogs = BlogPost.objects.filter(published=True).order_by('-created_at')[:3]  # hanya 3 blog terbaru
    return render(request, 'blog/index.html', {
        'skills': skills,
        'additional_skills': additional_skills,
        'projects': projects,
        'blogs': blogs,
    })

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'blog/project.html', {'projects': projects})

def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog/blog.html', {'posts': posts})

def contact(request):
    return render(request, 'blog/contact.html')