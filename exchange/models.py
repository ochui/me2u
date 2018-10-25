from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from .utils import unique_order_id_generator, unique_trade_id_generator

from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

class Trade(models.Model):
    """
    The Trade model handles offers request
    """
    TRADE_CHANNEL_CHOICES = (
        ('P2P', _('Peer to peer')),
        ('ESS', _('Escrow service'))
    )

    trade_uid = models.CharField(_("trade id"), max_length=10, null=True)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('buyer'), on_delete=models.CASCADE, blank=False, null=False)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name=_('offer'), blank=False, null=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('seller'), on_delete=models.CASCADE, blank=False, null=False, related_name='seller')
    amount = models.DecimalField(_('amount'), max_digits=19, decimal_places=10)
    rate_per_coin = models.DecimalField(_('rate per coin'), max_digits=19, decimal_places=10)
    payment_channel = models.CharField(_("payment channel"), max_length=50, choices=TRADE_CHANNEL_CHOICES, default='P2P')
    status = models.CharField(_('trade status'), max_length=8)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    expires = models.DateTimeField(_('expires'))

    def __str__(self):
        return _('%(buyer)s is buying %(offer)s from %(seller)s.') % {'buyer': self.buyer, 'offer': self.offer, 'seller': self.seller}

class Offer(models.Model):

    offer_id = models.CharField(_("offer id"), max_length=10, null=True)
    owner =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('owner'), related_name='offers')
    location = CountryField(_('location'), blank_label=_('select location'))
    coin = models.ForeignKey('Coin', on_delete=models.CASCADE, null=False, blank=False)
    rate_per_coin = models.DecimalField(_('rate per coin'), max_digits=19, decimal_places=10)
    minimum_amount = models.DecimalField(_('minimum amount'), max_digits=19, decimal_places=10)
    maximum_amount = models.DecimalField(_('maximum amount'), max_digits=19, decimal_places=10)
    terms = models.TextField(_('terms'))
    instructions = models.TextField(_('instructions'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return _('%(coin)s at the rate of %(rate)s per coin') % {'coin':self.coin, 'rate':self.rate_per_coin}

    def get_absolute_url(self):
        return reverse("user_offer_list")
    

class Coin(models.Model):

    name = models.CharField(_('name'), max_length=15)
    vendor = models.CharField(_('vendor'), max_length=100,)
    is_active = models.BooleanField(_('is active'), default=False )
    description = models.TextField(_('description'), blank=True, null=Trade)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return _('%(name)s') % {'name':self.name}


def pre_save_create_unique_offer_id(sender, instance, *args, **kwargs):

    if not instance.offer_id:
        instance.offer_id= unique_order_id_generator(instance)

pre_save.connect(pre_save_create_unique_offer_id, sender=Offer)

def pre_save_create_unique_trade_id(sender, instance, *args, **kwargs):

    if not instance.trade_uid:
        instance.trade_uid= unique_trade_id_generator(instance)

pre_save.connect(pre_save_create_unique_trade_id, sender=Trade)
