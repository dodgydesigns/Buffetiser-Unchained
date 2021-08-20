from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main, name='Buffetiser'),
    path('<symbol>/', views.investmentDetails, name='Investment Details'),

    path('config', views.config, name='Buffetiser Config'),
    path('help', views.help, name='Buffetiser Help'),
]