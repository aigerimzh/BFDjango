# Generated by Django 2.1.1 on 2018-10-29 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_restaurant_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
