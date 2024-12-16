from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Category, Item, Tag, Image

class ImageInline(GenericTabularInline):
    model = Image
    extra = 1

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    fields = ('name', 'price', 'description')
    readonly_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [ImageInline, ItemInline]

class TagInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    search_fields = ('name', 'description')
    ordering = ('-price',)
    inlines = [ImageInline, TagInline]

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
