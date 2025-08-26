from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'order', 'is_active']
    list_editable = ['price', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
