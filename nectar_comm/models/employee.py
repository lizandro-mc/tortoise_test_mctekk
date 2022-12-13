from tortoise import fields
from tortoise.contrib.pydantic import (
    pydantic_model_creator,
    pydantic_queryset_creator
)
from nectar_comm.models.communication_relationship import Employee as Relations


class Employee(Relations):
    
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)
    name = fields.CharField(max_length=100, null=True)

    class Meta:
        table = "employees"
        table_description = "Saved all info about the client"

Employee_Pydantic = pydantic_model_creator(Employee)
Employee_Pydantic_List = pydantic_queryset_creator(Employee)