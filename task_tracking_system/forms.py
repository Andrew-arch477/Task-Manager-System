from django import forms
from .models import Task, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Назва завдання",
                'autofocus': 'autofocus',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Опис завдання',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status', 'priority', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Назва завдання",
                'autofocus': 'autofocus',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class TaskFilterForm(forms.Form):
    name = forms.CharField(required=False)
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES, required=False)
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, required=False)

class User_Login_Form(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш коментар.',
            }),
        }

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        label='Username:',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
