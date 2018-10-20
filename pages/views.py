#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from exchange.models import Offer, Coin

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
    