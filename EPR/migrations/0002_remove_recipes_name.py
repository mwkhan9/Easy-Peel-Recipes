# Generated by Django 3.1 on 2020-08-08 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EPR', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='name',
        ),
    ]
