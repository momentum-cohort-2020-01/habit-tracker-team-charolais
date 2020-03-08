# Generated by Django 3.0.4 on 2020-03-06 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0006_auto_20200306_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitrecord',
            name='related_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_habit', to='habit_tracker.Habit'),
        ),
    ]