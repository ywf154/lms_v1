# Generated by Django 5.0.3 on 2024-04-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('organizations', '0003_alter_courseorg_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]