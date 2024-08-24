from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import ContactInfo, Product, NetworkEntity


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(NetworkEntity)
class NetworkEntityAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier_link', 'debt',)
    list_filter = ('contacts__city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', self.get_supplier_admin_url(obj.supplier), obj.supplier.title)
        return '-'

    supplier_link.short_description = 'Поставщик'

    def get_supplier_admin_url(self, supplier):
        url = reverse('admin:network_networkentity_change', args=[supplier.id])
        return url

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)
        self.message_user(request, 'Задолженность перед поставщиком была успешно обнулена.')

    clear_debt.short_description = 'Обнулить задолженность у выбранных объектов'
