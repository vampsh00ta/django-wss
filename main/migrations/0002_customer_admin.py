# Generated by Django 4.0.6 on 2022-07-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
