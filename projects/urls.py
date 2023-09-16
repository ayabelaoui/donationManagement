# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path("project", views.project, name='project'),
    path("projectIdx", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]