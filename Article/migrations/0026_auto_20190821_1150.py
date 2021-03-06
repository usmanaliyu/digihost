# Generated by Django 2.1.10 on 2019-08-21 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0025_article_test11'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='link_name',
            new_name='source1',
        ),
        migrations.RemoveField(
            model_name='article',
            name='link',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part1',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part3',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part4',
        ),
        migrations.RemoveField(
            model_name='article',
            name='part5',
        ),
        migrations.RemoveField(
            model_name='article',
            name='test11',
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='source10',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source2',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source3',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source4',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source5',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source6',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source7',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source8',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='source9',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
