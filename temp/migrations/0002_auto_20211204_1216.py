# Generated by Django 3.0.8 on 2021-12-04 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dato',
            old_name='name',
            new_name='valor',
        ),
    ]
