from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Client(TenantMixin):
    # Define your tenant model fields here
    name = models.CharField(max_length=100)
    # Add any additional fields you need

    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True) # Add a field to track trial status
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True


class Domain(DomainMixin):
    # Define your domain model fields here
    pass
