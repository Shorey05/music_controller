# Generated by Django 3.2.4 on 2021-08-31 14:19

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_guest_room_guest_can_pause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_code, max_length=8, unique=True),
        ),
    ]
