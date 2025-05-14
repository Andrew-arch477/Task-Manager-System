from task_tracking_system.models import Task
import django_filters



class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'name': ['icontains'], 
            'status': ['exact'], 
            'priority': ['exact']
        }
