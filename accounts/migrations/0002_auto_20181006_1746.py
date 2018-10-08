# Generated by Django 2.1.2 on 2018-10-06 17:46

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date of birth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(related_name='follower', through='contact.Contact', to=settings.AUTH_USER_MODEL, verbose_name='following'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=50, verbose_name='gender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/%Y/%m/%d/', verbose_name='avatar'),
        ),
    ]