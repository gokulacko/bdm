# Generated by Django 2.1.3 on 2019-01-07 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0001_initial'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='AckodriveDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_latest', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AckodriveKindOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offers', models.TextField(blank=True, null=True)),
                ('is_latest', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AckodriveQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('corporatediscount_id', models.BigIntegerField()),
                ('created_on', models.DateField()),
                ('updated_on', models.DateField()),
                ('ackodrivedicsount_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.AckodriveDiscount')),
            ],
        ),
        migrations.CreateModel(
            name='Bdm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=10)),
                ('alt_contact_no', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
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
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('contact_no_1', models.CharField(max_length=10)),
                ('contact_no_2', models.CharField(max_length=10, null=True)),
                ('is_primary_contact', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_company', models.CharField(max_length=30)),
                ('dealership_name', models.CharField(max_length=30)),
                ('status', models.CharField(default='Active', max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('sales_outlet', models.BooleanField(default=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('bdm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Bdm')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='DealerDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=8, max_digits=10)),
                ('is_latest', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.City')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='DealerOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offers', models.DecimalField(decimal_places=8, max_digits=10)),
                ('is_latest', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.City')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vehicle_type', models.CharField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('area', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('status', models.CharField(default='Active', max_length=30)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=50)),
                ('okind', models.CharField(max_length=50)),
                ('oid', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=10)),
                ('pg', models.CharField(max_length=100)),
                ('pg_token', models.CharField(max_length=100)),
                ('pg_response', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=30)),
                ('payment_on', models.CharField(max_length=30)),
                ('payment_method', models.CharField(max_length=30)),
                ('order_id', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
                ('created_on', models.DateField()),
                ('updated_on', models.DateField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Booking')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.AckodriveQuote')),
            ],
        ),
        migrations.CreateModel(
            name='PriceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_showroom', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registration_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insurance_premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('environment_compensation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('octroi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('depot_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rsa_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extended_warranty_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cash_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('basic_accessories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_plate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('smart_card', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mcd_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_collected_at_source', models.DecimalField(decimal_places=2, max_digits=10)),
                ('road_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_latest', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dealer.City')),
            ],
        ),
        migrations.CreateModel(
            name='PriceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rto_name', models.CharField(max_length=100)),
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
            name='TransmissionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cc', models.IntegerField(blank=True, null=True)),
                ('seating_capacity', models.IntegerField(blank=True, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('iscorporatediscount', models.BooleanField(default=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Model')),
                ('transmission_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dealer.TransmissionType')),
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
            model_name='priceconfig',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
        migrations.AddField(
            model_name='dealeroffer',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
        migrations.AddField(
            model_name='dealerdiscount',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
        migrations.AddField(
            model_name='contact',
            name='dealer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer'),
        ),
        migrations.AddField(
            model_name='contact',
            name='outlet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dealer.Outlet'),
        ),
        migrations.AddField(
            model_name='booking',
            name='testdrive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Testdrive'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='dealer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Dealer'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='dealerdiscount_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.DealerDiscount'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='insurancetype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.InsuranceType'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='outlet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Outlet'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='price_config_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.PriceConfig'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='pricetype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.PriceType'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='rto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Rto'),
        ),
        migrations.AddField(
            model_name='ackodrivequote',
            name='variant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
        migrations.AddField(
            model_name='ackodrivekindoffers',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.City'),
        ),
        migrations.AddField(
            model_name='ackodrivekindoffers',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
        migrations.AddField(
            model_name='ackodrivediscount',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.City'),
        ),
        migrations.AddField(
            model_name='ackodrivediscount',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.Variant'),
        ),
    ]
