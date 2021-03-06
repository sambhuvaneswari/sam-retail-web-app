# Generated by Django 3.0.10 on 2021-08-01 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Households',
            fields=[
                ('hshd_num', models.SmallIntegerField(db_column='HSHD_NUM', primary_key=True, serialize=False)),
                ('l', models.CharField(blank=True, db_column='L', max_length=10, null=True)),
                ('age_range', models.CharField(blank=True, db_column='AGE_RANGE', max_length=250, null=True)),
                ('marital', models.CharField(blank=True, db_column='MARITAL', max_length=250, null=True)),
                ('income_range', models.CharField(blank=True, db_column='INCOME_RANGE', max_length=250, null=True)),
                ('homeowner', models.CharField(blank=True, db_column='HOMEOWNER', max_length=250, null=True)),
                ('hshd_composition', models.CharField(blank=True, db_column='HSHD_COMPOSITION', max_length=250, null=True)),
                ('hh_size', models.CharField(blank=True, db_column='HH_SIZE', max_length=250, null=True)),
                ('children', models.CharField(blank=True, db_column='CHILDREN', max_length=250, null=True)),
            ],
            options={
                'db_table': 'households',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_num', models.IntegerField(db_column='PRODUCT_NUM', primary_key=True, serialize=False)),
                ('department', models.CharField(blank=True, db_column='DEPARTMENT', max_length=250, null=True)),
                ('commodity', models.CharField(blank=True, db_column='COMMODITY', max_length=250, null=True)),
                ('brand_ty', models.CharField(blank=True, db_column='BRAND_TY', max_length=250, null=True)),
                ('natural_organic_flag', models.CharField(blank=True, db_column='NATURAL_ORGANIC_FLAG', max_length=10, null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('basket_num', models.CharField(db_column='BASKET_NUM', max_length=250, primary_key=True, serialize=False)),
                ('purchase', models.DateField(blank=True, db_column='PURCHASE', null=True)),
                ('spend', models.DecimalField(blank=True, db_column='SPEND', decimal_places=2, max_digits=5, null=True)),
                ('units', models.IntegerField(blank=True, db_column='UNITS', null=True)),
                ('store_r', models.CharField(blank=True, db_column='STORE_R', max_length=250, null=True)),
                ('week_num', models.IntegerField(blank=True, db_column='WEEK_NUM', null=True)),
                ('year', models.IntegerField(blank=True, db_column='YEAR', null=True)),
                ('hshd_num', models.ForeignKey(blank=True, db_column='HSHD_NUM', null=True, on_delete=django.db.models.deletion.CASCADE, to='rwa.Households')),
                ('product_num', models.ForeignKey(blank=True, db_column='PRODUCT_NUM', null=True, on_delete=django.db.models.deletion.CASCADE, to='rwa.Products')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
