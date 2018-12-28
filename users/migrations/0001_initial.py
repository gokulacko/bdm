# Generated by Django 2.1.3 on 2018-12-27 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('home_address', models.TextField()),
                ('home_latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('home_longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('testdrive_address', models.TextField()),
                ('test_latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('test_longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('phone', models.CharField(default='Active', max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('role', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
    ]