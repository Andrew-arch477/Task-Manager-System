from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from task_tracking_system.models import Task, Comment
from task_tracking_system.forms import TaskForm
from task_tracking_system.filters import TaskFilter

class Task_main(ListView):
    queryset = Task.objects.all()
    template_name = 'Task_main.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter_set = TaskFilter(self.request.GET, queryset=queryset)
        return self.filter_set.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filter_set.form
        return context
        

class Task_Create(FormView):
    template_name = 'Task_create.html'
    form_class = TaskForm
    success_url = '/task_m/Task_main/'

    def form_valid(self, form):
        Task.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            priority=form.cleaned_data['priority'],
            deadline=form.cleaned_data['deadline']
        )
        return super().form_valid(form)   