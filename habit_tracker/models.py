from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    record = models.ForeignKey('HabitRecord', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    unit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__ (self):
        return f'name: {self.name} goal: {self.goal}'

class HabitRecord(models.Model):
    progress = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
