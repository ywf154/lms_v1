# Generated by Django 5.0.3 on 2024-03-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='', upload_to='head_image/%Y/%m', verbose_name='用户头像'),
        ),
    ]