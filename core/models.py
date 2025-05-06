from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target = models.CharField(max_length=255, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(null=True, blank=True)
    sets = models.PositiveIntegerField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.activity_type} on {self.date}"
