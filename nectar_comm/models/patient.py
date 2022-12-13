
from tortoise import fields
from tortoise.contrib.pydantic import (
    pydantic_model_creator,
    pydantic_queryset_creator
)
from nectar_comm.models.communication_relationship import Patient as Relations


class Patient(Relations):
    
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)
    name = fields.CharField(max_length=100, null=True)

    class Meta:
        table = "patients"
        table_description = "Saved all info about the client"

Patient_Pydantic = pydantic_model_creator(Patient)
Patient_Pydantic_List = pydantic_queryset_creator(Patient)