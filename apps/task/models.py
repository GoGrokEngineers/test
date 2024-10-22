from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Task(models.Model):  
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    difficulty = models.CharField(max_length=50)  # it can be choice field
    
    

    def __str__(self):
        return f"{self.title} - {self.difficulty}"
    
# class Submission(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     code = models.TextField()
#     language = models.CharField(max_length=20)
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     passed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Submission by {self.user.username} for {self.task.title}"
