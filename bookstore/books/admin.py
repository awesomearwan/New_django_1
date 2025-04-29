
# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price', 'is_visible')
    list_filter = ('is_visible', 'published_date')
    search_fields = ('title', 'author')
    list_editable = ('price', 'is_visible')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
