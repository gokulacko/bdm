# Generated by Django 2.1.3 on 2019-01-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0007_auto_20181231_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ackodrivekindoffers',
            name='type',
            field=models.TextField(),
        ),
    ]
