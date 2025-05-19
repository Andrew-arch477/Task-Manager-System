from django import forms
from .models import Task, Comment

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

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES, required=False)
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, required=False)
    name = forms.CharField(required=False)