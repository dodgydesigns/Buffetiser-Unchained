from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),

    path('', views.main, name='Buffetiser'),
    path('<symbol>/', views.investmentDetails, name='Investment Details'),
    path('purchase', views.newPurchase, name='New Purchase'),
    path('add_purchase', views.addPurchase, name='Add Purchase'),
    path('config', views.config, name='Buffetiser Config'),
    path('live', views.updateLivePrices, name='Live Prices'),
    path('buffetiserHelp', views.buffetiserHelp, name='Buffetiser Help'),
]
