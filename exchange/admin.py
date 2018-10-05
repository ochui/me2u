from django.contrib import admin
from .models import Coin, Offer, Trade

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor', 'is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['owner', 'coin', 'rate_per_coin', 'minimum_amount', 'maximum_amount', 'location']
    list_filter = ['coin', 'rate_per_coin', 'location']
    list_editable = ['rate_per_coin', 'minimum_amount', 'maximum_amount',]

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'seller', 'offer', 'status', 'created_at', 'expires']
    list_filter = ['offer', 'status', 'created_at', 'expires']
    list_editable = ['status', 'expires',]