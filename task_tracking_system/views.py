from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from task_tracking_system.models import Task, Comment
from task_tracking_system.forms import TaskForm, TaskFilterForm, TaskUpdateForm, User_Login_Form, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from task_tracking_system.mixins import UserIsOwnerMixin
from django.contrib.auth.forms import UserCreationForm

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

class Task_Create(LoginRequiredMixin, FormView):
    template_name = 'Task_create.html'
    form_class = TaskForm
    success_url = '/task/task_main/'

    def form_valid(self, form):
        Task.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            priority=form.cleaned_data['priority'],
            deadline=form.cleaned_data['deadline'],
            user_creator=self.request.user
        )
        return super().form_valid(form)

class Task_Update(LoginRequiredMixin, UserIsOwnerMixin, FormView):
    template_name = 'Task_update.html'
    form_class = TaskUpdateForm
    success_url = '/task/task_main/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        task_id = self.kwargs.get('pk')
        task = Task.objects.get(pk=task_id)
        kwargs['instance'] = task
        return kwargs

    def form_valid(self, form):
        form.save() 
        return super().form_valid(form)
    
    def get_object(self):
        task_id = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=task_id)

class Task_Delete(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = 'Task_delete.html'
    success_url = '/task/task_main/'

class Login_View(FormView):
    template_name = "Login.html"
    form_class = User_Login_Form
    success_url = '/task/task_main/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)

class Registration_View(FormView):
    template_name = "Registration.html"
    form_class = UserCreationForm
    success_url = '/task/login/'

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class Logout_View(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('/task/login/')

class Comment_Create_View(LoginRequiredMixin, FormView):
    template_name = 'Comment.html'
    form_class = CommentForm
    success_url = '/task/task_main/'

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        Comment.objects.create(
            text=form.cleaned_data['text'],
            user=self.request.user,
            task=self.task
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        context['comments'] = Comment.objects.filter(task=self.task)
        return context
