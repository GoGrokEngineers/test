import random
from apps.task.models import Task

def get_random(difficulty):
    tasks = Task.objects.filter(difficulty=difficulty)
    task = random.choice(tasks)
    return task
