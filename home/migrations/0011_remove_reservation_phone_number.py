# Generated by Django 5.0.1 on 2024-05-12 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='phone_number',
        ),
    ]
