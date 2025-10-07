from django.contrib import admin
from .models import Project,Skill,Contact
# Register your models here.
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Contact)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ("name", "category", "level", "order", "is_active")
    list_filter   = ("category", "is_active")
    search_fields = ("name",)
    list_editable = ("level", "order", "is_active")
    ordering      = ("category", "order", "-level")