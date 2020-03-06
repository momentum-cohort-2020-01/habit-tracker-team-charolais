from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import User, Habit
from .forms import HabitForm

def habit_list(request):
  habits = Habit.objects.all()
  return render(request, 'habit_tracker/habit_list.html', {'habits': habits})