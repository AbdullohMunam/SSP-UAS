from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project_list, name='project_list'),
    path('blog/', views.blog_list, name='blog_list'),
    path('contact/', views.contact, name='contact'),
]
