# Generated by Django 2.2.2 on 2019-07-10 07:34

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('listing', '0010_auto_20190710_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='products',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]