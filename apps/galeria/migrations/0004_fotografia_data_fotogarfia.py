# Generated by Django 4.1 on 2024-07-26 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0003_fotografia_publicado"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="data_fotogarfia",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
