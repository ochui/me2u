#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OfferCreationForm, TradeCreationForm
from exchange.models import Offer, Trade
from django.http import Http404
from django.utils.translation import gettext as _
from django.utils import timezone


class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    form_class = OfferCreationForm
    template_name = "dashboard/create_offer.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        return super().form_valid(form)


class OfferListView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = "dashboard/list_offer.html"
    context_object_name = 'offers'

    def get_queryset(self, **kwargs):
        return Offer.objects.filter(owner=self.request.user)


class TradeCreateView(LoginRequiredMixin, CreateView):
    model = Trade
    form_class = TradeCreationForm
    template_name = "dashboard/create_trade.html"
    offer = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offer"] = self.offer
        return context

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        # Get offer from request data
        queryset = Offer.objects.filter(offer_id=self.kwargs['offer_id'])
        try:
            # Get the single item from the filtered queryset
            self.offer = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return {
            'rate_per_coin': self.offer.rate_per_coin,
            'offer': self.offer
        }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.buyer = self.request.user
        self.object.seller = self.offer.owner
        self.object.rate_per_coin = self.offer.rate_per_coin
        if form.cleaned_data['payment_channel'] == 'P2P':
            self.object.status = 'wat'
        else:
            self.object.status = 'sat'
        
        self.object.expires = timezone.now()
        self.object.offer_id = self.offer.id

        return super().form_valid(form)

