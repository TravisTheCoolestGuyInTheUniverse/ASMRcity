# Generated by Django 3.1.1 on 2020-12-11 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asmrvideo',
            old_name='url',
            new_name='embed',
        ),
    ]
