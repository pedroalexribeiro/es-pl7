# Generated by Django 2.1.1 on 2018-11-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181102_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tweet_ammount',
            field=models.IntegerField(blank=True, default=10),
        ),
    ]
