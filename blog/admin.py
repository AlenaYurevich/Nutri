from django.contrib import admin
from .models import Post, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order', 'created_on')
    list_editable = ('order',)  # Позволяет редактировать порядок прямо в списке
    ordering = ('order',)
    filter_horizontal = ('tags',)  # удобный выбор тегов
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']  # для автодополнения
    prepopulated_fields = {'slug': ('name',)}  # автоматическое создание slug


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)