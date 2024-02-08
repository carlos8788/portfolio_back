from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'url_repo', 'url_capture', 'date']  # Incluir 'date' aquí

admin.site.register(Project, ProjectAdmin)

