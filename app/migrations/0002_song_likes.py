# Generated by Django 5.1.2 on 2024-10-15 06:45

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=banjo.models.IntegerField(default=0),
        ),
    ]
