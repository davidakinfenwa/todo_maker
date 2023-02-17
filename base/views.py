from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView,FormView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        user=form.save()
        if(user is not None):
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

        # this function redirect logged in user to the landing page 
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')

        return super(RegisterPage, self).get( *args, **kwargs)



class Tasklisk(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context_object_name=super().get_context_data(**kwargs)
        context_object_name['tasks']=context_object_name['tasks'].filter(user=self.request.user)
        context_object_name['count']=context_object_name['tasks'].filter(complete=False).count()

        # saving the search keyword to the search_input
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            # performing the search base on title
            context_object_name['tasks']=context_object_name['tasks'].filter(title__icontains=search_input)
            
            # keeping the last typed keyword in the search area if it not clared
            context_object_name['search_input']=search_input

        return context_object_name


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name='task'
    template_name='base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model=Task
    fields=['title', 'description','complete']
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')



class TaskDelete(LoginRequiredMixin, DeleteView):
    model=Task
    context_object_name='tasks'
    success_url=reverse_lazy('tasks')