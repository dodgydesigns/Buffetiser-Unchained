from django.contrib import admin

# Register your models here.
from buffetiser_main.models import Purchase, History, Investment

admin.site.register(Investment)
admin.site.register(Purchase)
admin.site.register(History)


