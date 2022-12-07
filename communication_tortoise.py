from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model


class Employee(Model):
    id = fields.IntField(pk=True)

class Client(Model):
    id = fields.IntField(pk=True)

class Patient(Model):
    id = fields.IntField(pk=True)

class Clinic(Model):
    id = fields.IntField(pk=True)


class Communication(Model):
    id = fields.IntField(pk=True)
    client_id =  fields.ForeignKeyRelation[Client] = fields.ForeignKeyField(
        "models.Client", related_name="communications"
    )
    employee_id = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    events: fields.ReverseRelation["Event"]

    class Meta:
        ordering = ["name"]
