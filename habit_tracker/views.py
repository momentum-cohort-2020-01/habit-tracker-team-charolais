from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import User, Habit
from .forms import HabitForm
