# Generated by Django 4.0.6 on 2022-07-19 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggy', '0005_alter_scholar_parent_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='scholar_Name',
        ),
    ]
