from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


"""
   MODELO QUE REPROSENTA UM TENANT
"""


class Client(TenantMixin):
    nome = models.CharField(max_length=100)
    trial = models.BooleanField()
    inicio_licenca = models.DateField(auto_now_add=True)
    inicio_fim = models.DateField(null=True)
    
    auto_create_schema = True


class Domain(DomainMixin):
    pass
