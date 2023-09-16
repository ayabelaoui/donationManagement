# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path("project", views.project, name='project'),
]