# Generated by Django 3.2.8 on 2021-10-21 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='atendee',
            new_name='attendees',
        ),
    ]
