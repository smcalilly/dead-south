# Generated by Django 3.2.6 on 2021-08-26 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dead_south', '0004_auto_20210819_0122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pk']},
        ),
    ]
