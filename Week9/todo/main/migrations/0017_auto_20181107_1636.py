# Generated by Django 2.1.3 on 2018-11-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_list_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Due Date'),
        ),
    ]
