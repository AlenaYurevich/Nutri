from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order', 'created_on')
    list_editable = ('order',)  # Позволяет редактировать порядок прямо в списке
    ordering = ('order',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
