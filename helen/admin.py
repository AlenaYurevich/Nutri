from django.contrib import admin
from .models import Service, ServiceItem


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1
    fields = ['text', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    inlines = [ServiceItemInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'is_active', 'order')
        }),
        ('Цены и сроки', {
            'fields': ('price', 'renewal_price', 'duration'),
        }),
        ('Оформление', {
            'fields': ('icon_class',),
            'classes': ('collapse',)
        }),
    )


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ['service', 'text', 'order']
    list_filter = ['service']