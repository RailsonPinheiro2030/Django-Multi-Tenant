from celery import shared_task
from .models import Client
from djangoTenants.celery_app.celery import app


@shared_task
def create_tenant(client_id):
    client = Client.objects.get(id=client_id)
    client.create_schema(check_if_exists=True, sync_schema=True)
    