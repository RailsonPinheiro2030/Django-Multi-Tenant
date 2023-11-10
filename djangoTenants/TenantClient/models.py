from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


"""
   MODELO QUE REPROSENTA UM TENANT
"""


class Client(TenantMixin):
    nome = models.CharField(max_length=100)
    
    
    auto_create_schema = True


class Domain(DomainMixin):
    pass
