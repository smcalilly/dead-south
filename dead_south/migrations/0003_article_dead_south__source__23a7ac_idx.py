# Generated by Django 3.2.6 on 2021-08-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dead_south', '0002_article_title'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['source_url'], name='dead_south__source__23a7ac_idx'),
        ),
    ]
