# Generated by Django 3.0.4 on 2020-03-06 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0007_habitrecord_related_habit'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='habit',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='habitrecord',
            unique_together={('due_date', 'related_habit')},
        ),
    ]
