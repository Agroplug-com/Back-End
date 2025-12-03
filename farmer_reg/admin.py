from django.contrib import admin
from .models import Farmer

# Register your models here.
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['reg_date','first_name','phone', 'lga']
    search_fields = ('lga','phone')
    list_filter = ('lga',)