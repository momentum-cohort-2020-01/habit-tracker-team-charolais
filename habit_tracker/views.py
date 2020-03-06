from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import User, Habit
from .forms import HabitForm

def habit_list(request):
  habits = Habit.objects.all()
  return render(request, 'habit_tracker/habit_list.html', {'habits': habits})


# There might be some naming missmatch you can change what ever you need

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habit_tracker/habit_detail.html', {"habit": habit, "pk": pk})


def habit_new(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect('habit_detail', pk=habit.pk)
    else:
        form = HabitForm()

    return render(request, 'habit_tracker/habit_new.html', {"form": form})

# This needs to be updated
# def record_edit(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     if request.method == 'POST':
#         form = HabitForm(request.POST, instance=habit)
#         if form.is_valid():
#             form.save()
#             return redirect('habit_detail', pk=habit.pk)
#     else:
#         form = HabitForm(instance=habit)
    
#     return render(request, 'habit_tracker/habit_edit.html', {"form": form})

def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit_list')