# Generated by Django 2.1.3 on 2018-12-08 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0015_ackodrivequote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField()),
                ('updated_on', models.DateField()),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.AckodriveQuote')),
            ],
        ),
        migrations.CreateModel(
            name='Testdrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_time_1', models.TimeField()),
                ('preferred_time_2', models.TimeField()),
                ('status', models.CharField(max_length=30)),
                ('created_on', models.DateField()),
                ('updated_on', models.DateField()),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.AckodriveQuote')),
            ],
        ),
        migrations.CreateModel(
            name='VariantCorporateDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='testdrive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Testdrive'),
        ),
    ]