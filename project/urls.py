from django.urls import path
from .views import get_projects, get_one_project

urlpatterns = [
    # tus otras urls
    path('', get_projects),
    path('<str:id>', get_one_project),
]
