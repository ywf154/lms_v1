# Generated by Django 5.0.3 on 2024-04-13 14:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('operations', '0003_task_grade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAsk',
        ),
    ]