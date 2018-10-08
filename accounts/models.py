#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _

from contact.models import Contact


class CustomUser(AbstractUser):
    
    PHONE_NUMBER_STATUS_CHOICES = (
        ('0', _('NOT VERIFIED')),
        ('1', _('VERIFIED'))
    )

    GENDER = (
        ('M', _('MALE')),
        ('F', _('FEMALE'))
    )

    avatar = models.ImageField(_("avatar"), upload_to='avatars/%Y/%m/%d/', blank=True)
    gender = models.CharField(_("gender"), max_length=50, choices=GENDER)
    date_of_birth = models.DateField(_("date of birth"), blank=False, null=False)
    country = models.CharField(_("country"), max_length=50)
    phone_number = models.CharField(_("phone number"), max_length=20, null=True, blank=True)
    phone_number_status = models.CharField(_("phone number status"), max_length=50, choices=PHONE_NUMBER_STATUS_CHOICES, default='0')
    following = models.ManyToManyField("self", verbose_name=_("following"), through=Contact, symmetrical=False, related_name='followers')


