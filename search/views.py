from django.shortcuts import render
from projects.models import Projects

# Create your views here.

def do_search(request):
    projects = Projects.objects.filter(name__icontains=request.GET['q'])
    return render(request, "projects.html", {"projects":projects})