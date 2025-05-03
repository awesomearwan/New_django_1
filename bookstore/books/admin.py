from django.contrib import admin
from .models import Book, Contact, profile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price', 'is_visible')
    list_filter = ('is_visible', 'published_date')
    search_fields = ('title', 'author')
    list_editable = ('price', 'is_visible')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)

@admin.register(profile)    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'address', 'about')
    search_fields = ('name', 'email', 'mobile' )
    ordering = ('-name',)