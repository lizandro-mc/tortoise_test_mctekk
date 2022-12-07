from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model


class Employee(Model):
    id = fields.IntField(pk=True)


class Patient(Model):
    id = fields.IntField(pk=True)


class Clinic(Model):
    id = fields.IntField(pk=True)


class Client(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    communications: fields.ReverseRelation["Communication"]

    class Meta:
        ordering = ["name"]


class Communication(Model):
    id = fields.IntField(pk=True)
    client = fields.ForeignKeyRelation[Client] = fields.ForeignKeyField(
        "models.Client", related_name="communications"
    )
    communication = fields.CharField(max_length=100)

    class Meta:
        ordering = ["communication"]


async def run():

    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    Communication_Pydantic = pydantic_model_creator(Communication)
    Communication_Pydantic_List = pydantic_queryset_creator(Communication)
    Client_Pydantic = pydantic_model_creator(Client)

    client_1 = await Client.create(name="Juan")
    await client_1.save()
 

    comm = await Communication(Communication="Client one", client_id=client_1.id).save()

    p = await Communication_Pydantic.from_tortoise_orm(await Communication.get(communication="Client one"))
    print("One Comm:", p.json(indent=4))

    # pt = await Tournament_Pydantic_List.from_queryset(Tournament.filter(events__id__isnull=False))
    # print("All tournaments without events:", pt.json(indent=4))

if __name__ == "__main__":
    run_async(run())
