from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task

# Create your views here.


class Tasklisk(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name='task'
    template_name='base/task.html'
