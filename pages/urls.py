#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="landing_home"),
    path('offer', views.OfferListView.as_view(), name='offer_list'),
]