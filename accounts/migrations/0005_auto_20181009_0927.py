# Generated by Django 2.1.2 on 2018-10-09 09:27

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181008_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='country'),
        ),
    ]
