from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project-thumbnail/')
    alt_text = models.CharField(max_length=100, blank=True, default="")  # default ditambahkan
    technologies = models.CharField(max_length=200, help_text="Comma separated, e.g. HTML,CSS", default="")
    detail_url = models.URLField(blank=True, default="")
    repo_url = models.URLField(blank=True, default="")
    demo_url = models.URLField(blank=True, default="")
    created_at = models.DateField(auto_now_add=True)

    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100, default="General", help_text="e.g. Web Development, UI/UX Design")
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default="No description provided.")
    icon_url = models.URLField(default="https://via.placeholder.com/40?text=")

    def __str__(self):
        return self.title

class AdditionalSkill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name