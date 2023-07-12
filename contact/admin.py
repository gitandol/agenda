from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'email', 'prefix', 'ddd', 'phone',
    ordering = '-id',
    search_fields = 'first_name', 'last_name', 'email', 'phone'
    list_per_page = 15
    list_max_show_all = 100
    list_editable = 'phone', 'email', 'prefix', 'ddd',
    list_display_links = 'first_name', 'last_name',


