from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Client, Domain

# Register your models here.
@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial', 'created_on')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
