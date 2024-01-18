# Generated by Django 5.0.1 on 2024-01-18 05:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_first_name_kata_customer_last_name_kata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
