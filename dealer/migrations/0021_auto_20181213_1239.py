# Generated by Django 2.1.3 on 2018-12-13 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0020_auto_20181213_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='brand',
            field=models.ForeignKey(default='Hyundai', on_delete=django.db.models.deletion.CASCADE, to='dealer.Brand'),
        ),
        migrations.AlterField(
            model_name='dealerpricefile',
            name='period',
            field=models.DateField(auto_now_add=True),
        ),
    ]