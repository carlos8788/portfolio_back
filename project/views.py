from django.http import JsonResponse
from .models import Project

def get_projects(request):
    projects = Project.objects.all()
    projects_data = [project.to_dict() for project in projects]
    
    return JsonResponse(projects_data, safe=False)
