from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def projects(request):
    return render(request, 'blog/project.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog_list(request):
    return render(request, 'blog/blog.html')