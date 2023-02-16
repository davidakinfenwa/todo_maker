from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

class Tasklisk(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name='task'
    template_name='base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')



class TaskDelete(LoginRequiredMixin, DeleteView):
    model=Task
    context_object_name='tasks'
    success_url=reverse_lazy('tasks')