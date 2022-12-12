from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model





class Patient(Model):
    id = fields.IntField(pk=True)

Patient_Pydantic = pydantic_model_creator(Patient)