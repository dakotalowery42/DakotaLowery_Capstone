from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proposal, Task

from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def proposal_detail(request, pk, format=None):
    """
    Retrieve a task by id.
    """
    try:
        # gets the name of the current Proposal by its ID
        post = Proposal.objects.get(pk=pk)
        # Finds all tasks that are linked to that proposal
        tasks = Task.objects.all().filter(task_id=post)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # Returns many results, because it's a queryset
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


def home(request):
    return render(request, 'pages/home.html')


@login_required
def add_proposal(request):
    if request.method == 'GET':
        return render(request, 'pages/add_proposal.html')
    elif request.method == 'POST':
        title = request.POST['title']
        project_description = request.POST['project_description']
        map_id = request.POST['map_id']
        project_date_start = request.POST['project_date_start']
        project_date_end = request.POST['project_date_end']
        proposals = Proposal.objects.create(
            title=title, project_description=project_description, map_id=map_id, project_date_start=project_date_start, project_date_end=project_date_end)
        return redirect('add_proposal')

@login_required
def add_task(request, id):
    details = Proposal.objects.get(id=id)
    gantt_title = request.POST['gantt_title']
    tasks = Task.objects.all()
    gantt_date_start = request.POST['gantt_date_start']
    gantt_date_end = request.POST['gantt_date_end']
    context = {
        "details": details,
        "tasks": tasks
    }
    Task.objects.create(taskItem=gantt_title, task_id=details,
                        gantt_date_start=gantt_date_start, gantt_date_end=gantt_date_end)
    return redirect('see_details', id=id)

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    details = Proposal.objects.get(id=task.task_id.id)
    task.delete()
    tasks = Task.objects.all()
    context = {
        "details": details,
        "tasks": tasks
    }
    return render(request, 'pages/details.html', context)

@login_required
def proposals(request):
    proposals = Proposal.objects.all()
    context = {
        'proposals': proposals
    }
    return render(request, 'pages/proposals.html', context)

@login_required
def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': proposals
    }
    return render(request, 'pages/add_proposals.html', context)


@login_required
def proposal_view(request, id):
    post = Proposal.objects.get(id=id)
    print(post)
    context = {
        "post": post,
    }
    return render(request, 'pages/proposal_view.html', context)

@login_required
def see_details(request, id):
    details = Proposal.objects.get(id=id)
    context = {
        "details": details,
        "tasks": tasks
    }
    return render(request, 'pages/details.html', {"details": details})

@login_required
def serialized(request):
    return render(request, 'pages/serialized.html')
