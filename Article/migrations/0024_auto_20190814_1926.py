# Generated by Django 2.1.10 on 2019-08-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0023_article_meta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='meta_description',
            field=models.TextField(),
        ),
    ]