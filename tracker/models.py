from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('completed', 'Completed')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class WorkSession(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.SET_NULL)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_seconds = models.PositiveIntegerField()

class FuturePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    target_date = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0)  # 0-100 %

class CompetitiveTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)  # e.g. Codeforces
    problem_name = models.CharField(max_length=200)
    solved_at = models.DateTimeField()
