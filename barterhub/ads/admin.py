from django.contrib import admin

# Register your models here.
from .models import Ad, ExchangeProposal

admin.site.register(Ad)
admin.site.register(ExchangeProposal)
