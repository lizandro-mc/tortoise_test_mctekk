from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model


class Client(Model):
    id = fields.IntField(pk=True)


Client_Pydantic = pydantic_model_creator(Client)
Client_Pydantic_List = pydantic_queryset_creator(Client)
