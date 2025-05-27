from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOICES = [
        ('I', 'In progress'),
        ('D', 'Done'),
        ('F', 'Faild'),
    ]

    PRIORITY_CHOICES = [
        ('U', 'Виконати Терміново / Complete urgently'),
        ('NU', 'Виконання не є терміновим  / Completion is not urgent'),
    ]

    name = models.CharField(max_length = 30, unique=True)
    description = models.CharField(max_length = 300)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='I')
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='U')
    deadline = models.DateField(null=True, blank=True)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)


    def __str__(self): 
        return self.name 

class Comment(models.Model):
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)