# Generated by Django 2.1.3 on 2018-11-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0005_dealer_sales_outlet'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_primary_contact',
            field=models.BooleanField(default=False),
        ),
    ]
