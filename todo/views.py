from django.shortcuts import render
from django.http import Http404
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

def index(request):
    if request.method == 'POST':
        task = Task(title=request.POST['title'], due_at=make_aware(parse_datetime(request.POST['due_at'])))
        task.save()

    if request.GET.get('order') == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')   

    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Task  # Task モデルを使っている前提です

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/detail.html', {'task': task})
