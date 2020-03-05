from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    name = models.CharField(max_length=50)
    goal = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f'name: {self.name} goal: {self.goal}'