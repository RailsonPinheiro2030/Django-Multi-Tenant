from django.shortcuts import render
from django_tenants.utils import schema_context
from client.models import Client, Domain

@schema_context(Client.schema_name)
def index(request):
    tenant_name = request.tenant.schema_name
    tenant = {
        'tenant': request.tenant,
    }
    
    
    return render(request, 'index.html', tenant)

