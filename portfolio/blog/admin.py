from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Project, BlogPost, Skill, AdditionalSkill

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['title', 'technologies', 'created_at']
    search_fields = ['title', 'technologies']
    list_filter = ['created_at']

@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ['title', 'published', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['published', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(AdditionalSkill)