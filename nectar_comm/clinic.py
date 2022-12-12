from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model



class Clinic(Model):
    id = fields.IntField(pk=True)

Clinic_Pydantic = pydantic_model_creator(Clinic)