# Generated by Django 5.0.4 on 2024-04-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_slot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingslot',
            name='expiration',
            field=models.DateTimeField(blank=True),
        ),
    ]
