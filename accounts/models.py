from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    
    PHONE_NUMBER_STATUS_CHOICES = (
        ('0', 'NOT VERIFIED'),
        ('1', 'VERIFIED')
    )

    avatar = models.ImageField(_("avatar"), upload_to='users/%Y/%m/%d/', blank=True)
    country = models.CharField(_("country"), max_length=50)
    phone_number = models.CharField(_("phone number"), max_length=20, null=True, blank=True)
    phone_number_status = models.CharField(_("phone number status"), max_length=50, choices=PHONE_NUMBER_STATUS_CHOICES, default='0')

