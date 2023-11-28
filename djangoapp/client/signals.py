from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  Client
from .task import create_tenant

@receiver(post_save, sender=Client)
def created_client(sender, instance, created, **kwargs):
    if created:
        if instance.schema_name != 'public':
            create_tenant.delay(instance.id)

