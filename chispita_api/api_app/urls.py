from django.urls import path
from .views import viewUsuario

urlpatterns = [
    path('api_app/', viewUsuario.as_view()),
]


