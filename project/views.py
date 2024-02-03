from django.http import JsonResponse, Http404
from .models import Project

def get_projects(request):
    projects = Project.objects.all()
    projects_data = [project.to_dict() for project in projects]
    
    return JsonResponse(projects_data, safe=False)

def get_one_project(request, id):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        raise Http404("El proyecto no existe")
    
    return JsonResponse(project.to_dict())