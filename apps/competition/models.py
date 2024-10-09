from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
import random, string
# Create your models here.


class Competition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # it will be uid
    participants = models.IntegerField()
    # difficulty = models.CharField(max_length=100) # it can be choice
    # topic = models.CharField(max_length=100) # it can be choice
    six_digit_link = models.CharField(max_length=6, unique=True, blank=True) # it can be deleted
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    duration = models.DurationField(default=datetime.timedelta(hours=1))


    def save(self, *args, **kwargs):
        if not self.six_digit_link:
            self.six_digit_link = self.generate_six_digit_link()
        super().save(*args, **kwargs)


    def generate_six_digit_link(self):
        return ''.join(random.choices(string.digits, k=6))

    def __str__(self):
        return f"{self.id}"
    

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    has_completed = models.BooleanField(default=False)
    submission_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} in {self.competition}"
