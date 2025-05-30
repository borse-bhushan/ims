"""
This model is used to store tenant information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from utils.functions import get_uuid
from base.db_models import BaseModel


class Tenant(BaseModel):
    """Represents a tenant organization within the system."""

    tenant_id = models.CharField(primary_key=True, default=get_uuid, max_length=36)

    tenant_code = models.CharField(max_length=256)
    tenant_name = models.CharField(max_length=256)
    tenant_desc = models.TextField(null=True, default=None)

    class Meta:
        db_table = "tenants"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "tenant_id": self.tenant_id,
            "tenant_code": self.tenant_code,
            "tenant_name": self.tenant_name,
            "tenant_desc": self.tenant_desc,
        }
