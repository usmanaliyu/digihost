# Generated by Django 2.2.2 on 2019-07-06 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'verbose_name': 'listing_category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana'), ('south Africa', 'South Africa'), ('Senigal', 'Senigal')], max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('segment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='listing.Listing_category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-company_name'],
            },
        ),
    ]
