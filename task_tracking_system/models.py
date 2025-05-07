from django.db import models

class Task(models.Model):
    STATUS_PENDING = 'I'
    STATUS_COMPLETED = 'D'
    STATUS_FAILD = 'F'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'In progress'),
        (STATUS_COMPLETED, 'Done'),
        (STATUS_FAILD, 'Faild'),
    ]

    PRIORITY_COMPLETE_URGENTLY = 'U'
    PRIORITY_COMPLETE_NOT_URGENT = 'NU'

    PRIORITY_CHOICES = [
        (PRIORITY_COMPLETE_URGENTLY, 'Виконати Терміново / Complete urgently'),
        (PRIORITY_COMPLETE_NOT_URGENT, 'Виконання не є терміновим  / Completion is not urgent'),
    ]

    name = models.CharField(max_length = 30, unique=True)
    description = models.CharField(max_length = 300)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=PRIORITY_COMPLETE_NOT_URGENT)
    due_date = models.DateField(null=True, blank=True)


    def __str__(self): 
        return self.name 



