#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from exchange.models import Offer, Trade


class OfferCreationForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = (
            'location', 'coin', 'rate_per_coin',
            'minimum_amount', 'maximum_amount',
            'terms', 'instructions'
        )
        context_object_name = 'form'

        widgets = {
            'rate_per_coin': forms.NumberInput(
                attrs={
                    'class': 'input-bordered',
                }
            ),
            'minimum_amount': forms.NumberInput(
                attrs={
                    'class': 'input-bordered',
                }
            ),
            'maximum_amount': forms.NumberInput(
                attrs={
                    'class': 'input-bordered'
                }
            ),
            'terms': forms.Textarea(
                attrs={
                    'class': 'input-bordered'
                }
            ),
            'instructions': forms.Textarea(
                attrs={
                    'class': 'input-bordered'
                }
            )
        }


class TradeCreationForm(forms.ModelForm):

    class Meta:
        model = Trade
        fields = (
            'payment_channel', 'amount'
        )

        context_object_name = 'form'

        widgets = {
            'amount': forms.NumberInput(
                attrs={
                    'class': 'input-bordered',
                }
            ),
            'payment_channel': forms.RadioSelect(
                
            )
        }
