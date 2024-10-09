# from django.db import models
# from apps.task.models import Task
# from apps.competition.models import User
# # Create your models here.

# class Task(models.Model):
#     uid = models.IntegerField()  # It should uid implemetation
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     difficulty = models.CharField(max_length=50)  # it can be choice field
    

#     def __str__(self):
#         return self.title
    
    
# class Submission(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     code = models.TextField()
#     language = models.CharField(max_length=20)
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     passed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Submission by {self.user.username} for {self.task.title}"
