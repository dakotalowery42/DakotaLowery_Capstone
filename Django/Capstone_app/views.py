from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proposal, Task


def home(request):
    return render(request, 'pages/home.html')


def add_proposal(request):
    if request.method == 'GET':
        return render(request, 'pages/add_proposal.html')
    elif request.method == 'POST':
        title = request.POST['title']
        project_description = request.POST['project_description']
        map_id = request.POST['map_id']
        project_date_start = request.POST['project_date_start']
        project_date_end = request.POST['project_date_end']
        gantt_title = request.POST['gantt_title']
        proposals = Proposal.objects.create(
            title=title, project_description=project_description, map_id=map_id, gantt_title=gantt_title, project_date_start=project_date_start, project_date_end=project_date_end)
        return redirect('add_proposal')


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
    return render(request, 'pages/details.html', context)


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


def proposals(request):
    proposals = Proposal.objects.all()
    context = {
        'proposals': proposals
    }
    return render(request, 'pages/proposals.html', context)


def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': proposals
    }
    return render(request, 'pages/add_proposals.html', context)


def proposal_view(request, id):
    post = Proposal.objects.get(id=id)
    return render(request, 'pages/proposal_view.html', {"post": post})


def see_details(request, id):
    details = Proposal.objects.get(id=id)
    # tasks = Task.objects.filter(taskid.id=id)
    context = {
        "details": details,
        "tasks": tasks
    }
    return render(request, 'pages/details.html', context)
