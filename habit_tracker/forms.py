from django import forms

from .models import Habit, HabitRecord

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'goal', 'unit')
        

class HabitRecordForm(forms.ModelForm):

    class Meta:
        model = HabitRecord
        fields = ('related_habit', 'progress', 'due_date')