#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source 
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from exchange.models import Coin


class Wallet(models.Model):
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("owner"), on_delete=models.CASCADE)
    name = models.CharField(_('wallet name'), max_length=25)
    address = models.CharField(_("address"), max_length=255)
    crypto = models.ForeignKey(Coin, verbose_name=_("Crypto currency"), on_delete=models.CASCADE)

    def __str__(self):
        return _('%(owner)s %(crypto)s wallet') % {'owner':self.owner, 'crypto':self.crypto}
    