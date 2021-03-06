# Generated by Django 2.1.2 on 2018-10-05 21:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_auto_20181005_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='maximum_amount',
            field=models.DecimalField(decimal_places=10, max_digits=19, verbose_name='maximum amount'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]
