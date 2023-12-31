# Generated by Django 3.2.21 on 2023-10-17 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vyaparapp', '0004_auto_20231009_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_code', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField(blank=True, max_length=255, null=True)),
                ('End_date', models.DateField(blank=True, max_length=255, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=255, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='image/patient')),
                ('Action', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='payment_terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_terms_number', models.IntegerField(blank=True, null=True)),
                ('payment_terms_value', models.CharField(blank=True, max_length=100, null=True)),
                ('days', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='modules_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_invoice', models.CharField(default=0, max_length=100, null=True)),
                ('Estimate', models.IntegerField(default=0, null=True)),
                ('Payment_in', models.IntegerField(default=0, null=True)),
                ('sales_order', models.IntegerField(default=0, null=True)),
                ('Delivery_challan', models.IntegerField(default=0, null=True)),
                ('sales_return', models.IntegerField(default=0, null=True)),
                ('Purchase_bills', models.IntegerField(default=0, null=True)),
                ('Payment_out', models.IntegerField(default=0, null=True)),
                ('Purchase_order', models.IntegerField(default=0, null=True)),
                ('Purchase_return', models.IntegerField(default=0, null=True)),
                ('Bank_account', models.IntegerField(default=0, null=True)),
                ('Cash_in_hand', models.IntegerField(default=0, null=True)),
                ('cheques', models.IntegerField(default=0, null=True)),
                ('Loan_account', models.IntegerField(default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='dateperiod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.payment_terms'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staff_details',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company'),
        ),
        migrations.DeleteModel(
            name='company_details',
        ),
    ]
