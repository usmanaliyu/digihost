# Generated by Django 2.2.2 on 2001-01-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0019_auto_20190714_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='terms',
            field=models.CharField(choices=[('yes', 'Yes')], default=1, max_length=50, verbose_name='I agree to Terms and Conditions'),
        ),
    ]
