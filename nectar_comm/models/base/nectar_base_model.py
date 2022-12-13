from tortoise.models import Model
from tortoise import fields
from enum import Enum

# Note: Commons and specific fields in nectar models


class NectarBaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Named():
    name = fields.CharField(max_length=100, null=True)
