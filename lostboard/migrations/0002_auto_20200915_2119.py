# Generated by Django 3.0.5 on 2020-09-15 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lostboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='lostpost',
            new_name='post'
        )
    ]
