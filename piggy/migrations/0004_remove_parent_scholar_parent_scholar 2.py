# Generated by Django 4.0.6 on 2022-07-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggy', '0003_room_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='scholar',
        ),
        migrations.AddField(
            model_name='parent',
            name='scholar',
            field=models.ManyToManyField(to='piggy.scholar'),
        ),
    ]