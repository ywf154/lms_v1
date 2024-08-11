# Generated by Django 5.0.3 on 2024-08-11 18:35

import DjangoUeditor.models
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='城市名')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='OrgCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='机构类别名')),
            ],
            options={
                'verbose_name': '机构类别',
                'verbose_name_plural': '机构类别',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='描述')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')),
                ('address', models.CharField(max_length=150, verbose_name='机构地址')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.city', verbose_name='所在城市')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.orgcategory', verbose_name='机构类别')),
            ],
            options={
                'verbose_name': '机构',
                'verbose_name_plural': '机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='教师名')),
                ('work_years', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=50, verbose_name='就职公司')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('image', models.ImageField(default='teacher_img_default.jpg', upload_to='teacher/%Y/%m', verbose_name='头像')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.org', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
