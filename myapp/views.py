from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)

def about(request):
    return HttpResponse("About !!!")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)
