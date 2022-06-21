from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


# Create your views here.
projectslist = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where i built out my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project i am still working on'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(pk=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project,)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)


# def createProject(request):
#     form = ProjectForm()

#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     context = {'form': form}
#     return render(request, 'projects/project_form.html', context)


# def updateProject(request, pk):
#     project = Project.objects.get(id=pk)
#     form = ProjectForm(instance=project)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     context = {'form': form}
#     return render(request, 'projects/project_form.html.', context)


# def deleteProject(request, pk):
#     project = Project.objects.get(id=pk)
#     if request.method == 'POST':
#         project.delete()
#         return redirect('projects')
#     context = {'object': project}
#     return render(request, 'projects/delete_template.html', context)