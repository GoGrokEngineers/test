import csv
from apps.task.models import Task


def import_tasks_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Task.objects.get_or_create(
                title=row['title'],
                description = row['description'],
                difficulty=row['difficulty']
            )