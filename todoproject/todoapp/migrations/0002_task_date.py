# Generated by Django 4.1.3 on 2022-12-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-6-7'),
            preserve_default=False,
        ),
    ]
