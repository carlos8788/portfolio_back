from django.urls import path
from .views import get_csrf_token, LoginAPIView

urlpatterns = [
    path('get-csrf-token/', get_csrf_token),
    path('', LoginAPIView.as_view(), name='login'),
]
