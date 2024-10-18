from django.db import models
from apps.task.models import Task
import uuid
import datetime
import random, string
from django.utils import timezone

DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]


DURATION_CHOICES = [
        (1, '1 minute'),
        (5, '5 minutes'),
        (10, '10 minutes'),
        (15, '15 minutes'),
        (30, '30 minutes'),
        (60, '1 hour'),
    ]


class Competition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # it will be uid
    participants = models.IntegerField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, blank=True) # it can be choice
    six_digit_link = models.CharField(max_length=6, unique=True, blank=True) # it can be deleted
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, blank=False)
    duration_minutes = models.IntegerField(choices=DURATION_CHOICES, blank=False, null=False)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.six_digit_link:
            self.six_digit_link = self.generate_six_digit_link()
        super().save(*args, **kwargs)
        self.update_is_active()

    def generate_six_digit_link(self):
        return ''.join(random.choices(string.digits, k=6))

    def update_is_active(self):
        duration = datetime.timedelta(minutes=self.duration_minutes)
        if timezone.now() >= self.created_at + duration:
            self.is_active = False
            self.save()  # Save the updated status

    def __str__(self):
        return f"Competition {self.id} - Difficulty: {self.difficulty} - Active: {self.is_active}"
    

# class Participant(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
#     has_completed = models.BooleanField(default=False)
#     submission_time = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user.username} in {self.competition}"
