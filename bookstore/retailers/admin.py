
# Register your models here.
from django.contrib import admin
from .models import Retailer

@admin.register(Retailer)
class RetailderAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_no', 'date_of_joining', 'total_sales', 'address','is_active')
    list_filter = ('is_active', 'date_of_joining')
    search_fields = ('name', 'mobile_no')
    list_editable = ('total_sales', 'is_active','address','mobile_no')
    date_hierarchy = 'date_of_joining'
    ordering = ('-date_of_joining',)

