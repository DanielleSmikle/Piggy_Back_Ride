# Generated by Django 4.0.6 on 2022-07-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggy', '0016_alter_scholar_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='photo_url',
            field=models.TextField(default='https://tse1.mm.bing.net/th?id=OIP.o-paU20ODu6RRuU9ZIMCcQHaHa&pid=Api&P=0'),
        ),
    ]
