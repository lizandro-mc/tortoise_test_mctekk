from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model

class Communication(Model):
    id = fields.IntField(pk=True)
    communication = fields.CharField(max_length=500, null=True)
    contact_datetime = fields.DatetimeField(auto_now=True, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    clinics = fields.ReverseRelation("Clinic")
    class Meta:
        table = "Communication"

    def __str__(self):
        return f"{self.id}"

Communication_Pydantic = pydantic_model_creator(Communication)
Communication_Pydantic_list = pydantic_queryset_creator(Communication)