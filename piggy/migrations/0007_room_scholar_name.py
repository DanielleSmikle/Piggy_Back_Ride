# Generated by Django 4.0.6 on 2022-07-19 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggy', '0006_remove_room_scholar_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='scholar_Name',
            field=models.CharField(default='Billy Bob', max_length=100),
        ),
    ]
