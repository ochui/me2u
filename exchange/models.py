from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _

class Trade(models.Model):
    """
    The Trade model handles offers request
    """

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('buyer'), on_delete=models.CASCADE, blank=False, null=False)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name=_('offer'), blank=False, null=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('seller'), on_delete=models.CASCADE, blank=False, null=False, related_name='seller')
    amount = models.DecimalField(_('amount'), max_digits=19, decimal_places=10)
    rate_per_coin = models.DecimalField(_('rate per coin'), max_digits=19, decimal_places=10)
    status = models.CharField(_('trade status'), max_length=8)
    expires = models.DateTimeField(_('expires'))

    def __str__(self):
        return _('%(buyer)s is buying %(offer)s from %(seller)s.') % {'buyer': self.buyer, 'offer': self.offer, 'seller': self.seller}

class Offer(models.Model):

    
    owner =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('owner'), related_name='offers')
    location = models.CharField(_('location'), max_length=15)
    coin = models.ForeignKey('Coin', on_delete=models.CASCADE, null=False, blank=False)
    rate_per_coin = models.DecimalField(_('rate per coin'), max_digits=19, decimal_places=10)
    minimum_amount = models.DecimalField(_('minimum amount'), max_digits=19, decimal_places=10)
    maximum_amount = models.DecimalField(_('maximum_amount'), max_digits=19, decimal_places=10)
    terms = models.TextField(_('terms'))
    instructions = models.TextField(_('instructions'))
    created_at = models.DateTimeField(_('created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return _('%(coin)s at the rate of %(rate)s per coin') % {'coin':self.coin, 'rate':self.rate_per_coin}

class Coin(models.Model):

    name = models.CharField(_('name'), max_length=15)
    vendor = models.CharField(_('vendor'), max_length=100,)
    is_active = models.BooleanField(_('is active'), default=False )
    description = models.TextField(_('description'), blank=True, null=Trade)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return _(self.name)