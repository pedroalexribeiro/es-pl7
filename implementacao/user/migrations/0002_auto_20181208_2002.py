# Generated by Django 2.1.4 on 2018-12-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='orcid_token',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='research_group',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
