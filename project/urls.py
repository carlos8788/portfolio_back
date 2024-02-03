from django.urls import path
from .views import get_projects

urlpatterns = [
    # tus otras urls
    path('', get_projects),
]
