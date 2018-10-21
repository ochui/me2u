#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from exchange.models import Offer, Coin
from django.http import Http404
from django.utils.translation import gettext as _

class HomeView(TemplateView):
    
    template_name = 'landing/home.html'

class OfferListView(ListView):
    
    model = Offer
    template_name = 'landing/offer_list.html'
    context_object_name = 'offers'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coins"] = Coin.objects.all()
        return context

class OfferDetailView(DetailView):

    model = Offer
    template_name = "landing/offer_details.html"

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        """
        if queryset is None:
            queryset = self.get_queryset()

        #Get logged in user from request data
        queryset = queryset.filter(offer_id=self.kwargs['offer_id'])
        
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj
        
    
