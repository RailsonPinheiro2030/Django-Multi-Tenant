from django.contrib import admin
from .models import Client, Domain
from django_tenants.admin import TenantAdminMixin



class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.tenant.schema_name == 'public'


admin.site.register(Client, ClientAdmin)
admin.site.register(Domain, ClientAdmin)