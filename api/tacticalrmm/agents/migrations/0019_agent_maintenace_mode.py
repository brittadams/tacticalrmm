# Generated by Django 3.1.2 on 2020-10-25 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0018_auto_20201023_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='maintenace_mode',
            field=models.BooleanField(default=False),
        ),
    ]
