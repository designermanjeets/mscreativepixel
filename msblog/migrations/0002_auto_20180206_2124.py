# Generated by Django 2.0.2 on 2018-02-06 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.AlterModelOptions(
            name='headernavs',
            options={'verbose_name_plural': 'HeaderNavs'},
        ),
    ]
