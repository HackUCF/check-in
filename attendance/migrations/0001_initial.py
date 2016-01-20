# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('name', 'datetime')]),
        ),
        migrations.AddField(
            model_name='attendee',
            name='events',
            field=models.ManyToManyField(related_name='attendees', through='attendance.Attendance', to='attendance.Event'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='attendance.Attendee'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='attendance.Event'),
        ),
    ]