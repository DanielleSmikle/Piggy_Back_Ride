# Generated by Django 4.0.6 on 2022-07-20 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggy', '0017_alter_room_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar',
            name='Friday',
        ),
        migrations.RemoveField(
            model_name='scholar',
            name='Monday',
        ),
        migrations.RemoveField(
            model_name='scholar',
            name='Thursday',
        ),
        migrations.RemoveField(
            model_name='scholar',
            name='Tuesday',
        ),
        migrations.RemoveField(
            model_name='scholar',
            name='Wednesday',
        ),
    ]
