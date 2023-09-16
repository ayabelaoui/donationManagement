from django.shortcuts import render
from projects.models import ProjectSite


# Create your views here.
def project(request):
    return render(request, "project.html", {})

def project_index(request):
    projects = ProjectSite.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = ProjectSite.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)