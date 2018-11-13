#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.urls import path
from . import views

urlpatterns = [
    path('offer', views.OfferListView.as_view(), name="user_offer_list"),
    path('offer/create', views.OfferCreateView.as_view(), name='user_create_offer'),
    path("trade", views.TradeListView.as_view(), name="user_trade_list"),
    path("trade/<trade_id>", views.TradeDetailView.as_view(), name="user_trade_details"),
    path('trade/create/<offer_id>', views.TradeCreateView.as_view(), name="user_create_trade")
]