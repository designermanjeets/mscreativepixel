# Generated by Django 2.0.2 on 2018-02-08 15:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('msblog', '0008_auto_20180207_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=40, unique=True),
        ),
    ]
