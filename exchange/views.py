#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OfferCreationForm
from exchange.models import Offer


class OfferCreateView(LoginRequiredMixin ,CreateView):
    model = Offer
    form_class = OfferCreationForm
    template_name = "dashboard/create_offer.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        return super().form_valid(form)
