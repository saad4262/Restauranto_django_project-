# Generated by Django 5.0.1 on 2024-05-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='phone_no',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
