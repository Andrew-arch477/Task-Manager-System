from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from task_tracking_system.models import Task, Comment
from task_tracking_system.forms import TaskForm, TaskFilterForm, TaskUpdateForm

class Task_ViewPage(ListView):
    model = Task
    template_name = 'Task_main.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = Task.objects.all()
        self.form = TaskFilterForm(self.request.GET)

        if self.form.is_valid():
            data = self.form.cleaned_data

            name = data.get("name")
            status = data.get("status")
            priority = data.get("priority")


            if name:
                queryset = queryset.filter(name__icontains=name)
            if status:
                queryset = queryset.filter(status=status)
            if priority:
                queryset = queryset.filter(priority=priority)

            return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
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

class Task_Update(FormView):
    template_name = 'Task_update.html'
    form_class = TaskUpdateForm
    success_url = '/task_m/Task_main/'

    def form_valid(self, form):
        task_id = self.kwargs.get('pk')

        task = Task.objects.get(pk=task_id)
        task.name=form.cleaned_data['name']
        task.status=form.cleaned_data['status']
        task.priority=form.cleaned_data['priority']
        task.deadline=form.cleaned_data['deadline']
        task.save()
        return super().form_valid(form)