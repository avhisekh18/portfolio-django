from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title
    

class Skill(models.Model):
    TECH = "tech"
    PROF = "prof"
    CATEGORY_CHOICES = [(TECH, "Technical"), (PROF, "Professional")]

    name      = models.CharField(max_length=100)
    level     = models.PositiveIntegerField(help_text="0–100")
    category  = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=TECH)
    order     = models.PositiveIntegerField(default=0, help_text="Smaller shows first")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "order", "-level", "name"]

    def __str__(self):
        return f"{self.name} ({self.level}%)"

    def clean(self):
        if self.level > 100:
            raise ValidationError({"level": "Level must be between 0 and 100."})
    

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name