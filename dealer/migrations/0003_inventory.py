# Generated by Django 2.1.3 on 2018-12-28 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_auto_20181226_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(max_length=30)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant')),
            ],
        ),
    ]