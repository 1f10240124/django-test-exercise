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

def test_detail_get_success(self):
    task = Task(title='task1', due_at=timezone.make_aware(datetime(2024, 7, 1)))
    task.save()
    client = Client()
    response = client.get('/{}/'.format(task.pk))

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.templates[0].name, 'todo/detail.html')
    self.assertEqual(response.context['task'], task)

def test_detail_get_fail(self):
    client = Client()
    response = client.get('/1/')

    self.assertEqual(response.status_code, 404)
