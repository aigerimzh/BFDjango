# Generated by Django 2.1.1 on 2018-09-17 02:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_list_createted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListCompl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('createted_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
