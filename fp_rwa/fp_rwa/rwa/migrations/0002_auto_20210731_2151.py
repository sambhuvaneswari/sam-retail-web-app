# Generated by Django 3.0.10 on 2021-08-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transactions',
            name='basket_num',
            field=models.CharField(db_column='BASKET_NUM', max_length=250),
        ),
    ]