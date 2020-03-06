from django.db import models
from django.contrib.auth.models import User
import time
from datetime import date

class Habit(models.Model):
    record = models.ForeignKey('HabitRecord', on_delete=models.CASCADE, null=True, blank=True, related_name='habit_record')
    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    unit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today())
    owner = models.ForeignKey(to=User, related_name='owner', on_delete=models.CASCADE)
    observer = models.ForeignKey(to=User, related_name='observer', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('due_date', 'record')

    def __str__ (self):
        return self.name

class HabitRecord(models.Model):
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, null=True, blank=True, related_name='related_habit')
    progress = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default=date.today())

    def __str__ (self):
        return f'This is the record for {self.related_habit}.'