from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Todolist
from project.models import Project
from django.shortcuts import redirect
# Create your views here.

@login_required
def todolist(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    return render(request, 'todolist/todolist.html', {'todolist': todolist, 'project': project})

@login_required
def add(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk = project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Todolist.objects.create(name=name, description=description, created_by=request.user, project_id=project_id)
            return redirect(f'/projects/{project_id}/')
        else:
            print('Not valid')
    return render(request, 'todolist/add.html')

@login_required
def edit(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            project.name = name
            project.description = description
            project.save()
            return redirect(f'/projects/{pk}/')
        else:
            print('Not valid')
    return render(request, 'project/edit.html', {'project': project})
