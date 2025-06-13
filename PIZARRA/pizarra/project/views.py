from django.shortcuts import render, redirect
from .models import Project, ProjectFile
from django.contrib.auth.decorators import login_required
from .forms import ProjectFileForm

# Create your views here.
@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'project/projects.html', {'projects': projects})

@login_required
def project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(id=pk)
    return render(request, 'project/project.html', {'project': project})


@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        description = request.POST.get('description','')

        if name:
            project = Project.objects.create(name=name, description=description, created_by=request.user)
            return redirect('/projects/')
        else:
            print('Not valid')
        project.save()
        return render(request, 'project/add_project.html', {'message': 'Please create project.'})
    return render(request, 'project/add.html')

@login_required
def edit(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            project.name = name
            project.description = description
            project.save()

            return redirect(f'/projects/{pk}/')
        
    return render(request, 'project/edit.html', {'project': project})

@login_required
def delete(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    project.delete()
    return redirect('/projects/')


@login_required
def upload_file(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProjectFileForm(request.POST, request.FILES)

        if form.is_valid():
            projectfile = form.save(commit=False)
            projectfile.project = project
            projectfile.save()

            return redirect(f'/projects/{pk}/')
    else:
        form = ProjectFileForm()

    return render(request, 'project/upload_file.html', {
        'project': project,
        'form': form
    })

@login_required
def delete_file(request, pk, file_pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    projectfile = ProjectFile.objects.get(pk=file_pk)
    projectfile.delete()
    return redirect(f'/projects/{pk}/')