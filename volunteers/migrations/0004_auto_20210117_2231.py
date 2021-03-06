# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-17 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_merge_20210117_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteercategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='volunteercategory',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='taskcategory',
            name='volunteers',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='categories',
        ),
        migrations.AlterField(
            model_name='task',
            name='edition',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='volunteers.Edition'),
        ),
        migrations.AlterField(
            model_name='track',
            name='edition',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='volunteers.Edition'),
        ),
        migrations.AlterField(
            model_name='volunteerstatus',
            name='edition',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='volunteers.Edition'),
        ),
        migrations.DeleteModel(
            name='VolunteerCategory',
        ),
    ]
