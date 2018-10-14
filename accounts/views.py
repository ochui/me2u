#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.http import Http404
from django.utils.translation import gettext as _
from allauth.account.models import EmailAddress
from .models import CustomUser
from .forms import AccountEditForm
from wallet.models import Wallet
from exchange.models import Coin

class UserDashboard(LoginRequiredMixin, TemplateView):
    
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #check user email status
        if not EmailAddress.objects.filter(user=self.request.user, verified=True).exists():
            context['verified_email'] = False
        else:
            context['verified_email'] = True
                
        return context

class UserAccountDetails(LoginRequiredMixin, UpdateView):
    
    template_name = 'dashboard/account_edit.html'
    context_object_name = 'form'
    form_class = AccountEditForm
    #fields = ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'country')
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not EmailAddress.objects.filter(user=self.request.user, verified=True).exists():
            context['verified_email'] = False
        else:
            context['verified_email'] = True
        
        #Get Supported Crypto
        coins = Coin.objects.all()
        context['coins'] = coins
        return context
    
    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        """
        if queryset is None:
            queryset = self.get_queryset()

        #Get logged in user from request data
        queryset = queryset.filter(pk=self.request.user.id)
        
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj
        