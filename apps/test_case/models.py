from django.db import models
from apps.task.models import Task

class TestCase(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="tasks")
    input = models.TextField()
    output = models.TextField()
    input_type = models.CharField(max_length=50)
    output_type = models.CharField(max_length=50)
