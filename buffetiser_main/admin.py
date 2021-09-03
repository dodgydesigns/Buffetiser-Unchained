from django.contrib import admin

# Register your models here.
from buffetiser_main.models import Purchase, History

admin.site.register(Purchase)
admin.site.register(History)


