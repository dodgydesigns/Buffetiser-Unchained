from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='Buffetiser'),
    path('config', views.config, name='Buffetiser Config'),
    path('help', views.help, name='Buffetiser Help'),
]