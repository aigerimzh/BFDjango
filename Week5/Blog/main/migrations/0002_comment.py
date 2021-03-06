# Generated by Django 2.1.2 on 2018-10-06 08:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=200)),
                ('text_com', models.TextField()),
                ('com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.Blog')),
            ],
        ),
    ]
