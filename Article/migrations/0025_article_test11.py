# Generated by Django 2.1.10 on 2019-08-14 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0024_auto_20190814_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='test11',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
