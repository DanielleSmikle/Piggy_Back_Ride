# Generated by Django 4.0.6 on 2022-07-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggy', '0002_alter_scholar_parent_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photo_url',
            field=models.TextField(default='https://tse3.mm.bing.net/th?id=OIP.sttsR_82WRk0u7zA7lpGPAHaFN&pid=Api&P=0&w=255&h=179'),
        ),
    ]