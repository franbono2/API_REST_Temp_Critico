# Generated by Django 3.2.9 on 2021-12-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('time', models.BigIntegerField(primary_key=True, serialize=False)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]
