# Generated by Django 3.0.5 on 2020-09-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostboard', '0003_auto_20200916_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
