# Generated by Django 3.2.2 on 2021-05-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mode',
            name='name',
        ),
    ]
