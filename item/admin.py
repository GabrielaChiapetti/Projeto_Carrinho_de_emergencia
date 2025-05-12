from django.contrib import admin

from item import models

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'expiration_date','amount', 'created_date', 'show',)
    ordering = ('expiration_date',)
    search_fields = ('id', 'item', 'expiration_date',)
    list_editable = ('expiration_date', 'amount',)
    list_display_links = ('item',)
    list_per_page = 10
    list_max_show_all = 200
    


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_max_show_all = 200
    ...