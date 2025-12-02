from django.contrib import admin
from .models import Buyer

# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone','lga', 'reg_date']
    search_fields = ['lga','first_name']
    list_filter = ['lga']