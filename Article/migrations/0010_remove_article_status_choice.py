# Generated by Django 2.2.2 on 2019-07-04 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0009_article_status_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='STATUS_CHOICE',
        ),
    ]
