# Generated by Django 3.1.1 on 2020-09-15 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactformresponses',
            old_name='email_id',
            new_name='email',
        ),
    ]