# Generated by Django 4.0.3 on 2022-04-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_total_gross_profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_due', models.DateField()),
                ('amount_total_company_currency', models.DecimalField(decimal_places=2, max_digits=10)),
                ('partner_code', models.CharField(max_length=50)),
                ('partner_name', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=5)),
                ('date_invoice', models.DateField()),
                ('amount_untaxed_company_currency', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_tax_company_currency', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_residual_company_currency', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
