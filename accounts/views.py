#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from allauth.account.models import EmailAddress

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
