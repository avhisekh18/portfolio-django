from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title
    

class Skill(models.Model):
    name= models.CharField(max_length=30)
    level = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name