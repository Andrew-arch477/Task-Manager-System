from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from task_tracking_system.models import Task, Comment
from task_tracking_system.forms import TaskForm

class Task_main(TemplateView):
    template_name = 'Task_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
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