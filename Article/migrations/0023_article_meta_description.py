# Generated by Django 2.1.10 on 2019-08-13 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0022_auto_20190813_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]