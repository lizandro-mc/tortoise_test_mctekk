from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model


class Employee(Model):
    id = fields.IntField(pk=True)


class Patient(Model):
    id = fields.IntField(pk=True)


class Clinic(Model):
    id = fields.IntField(pk=True)
# Event


class Client(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    communications: fields.ManyToManyRelation["Communication"] = fields.ManyToManyField(
        "models.Communication", related_name="clients", through="client_communication"
    )

    def __str__(self):
        return self.name


# Team


class Communication(Model):
    id = fields.IntField(pk=True)
    communication = fields.TextField()

    clients = fields.ManyToManyRelation[Client]

    class Meta:
        ordering = ["communication"]


async def run():

    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    comms = []

    for i in range(0, 10):
        communication = Communication(communication=f"Comm test {i +1}!")
        await communication.save()
        print(f"Print comm {i}: ", communication.id)
        comms.append(communication)

    client = Client(
        name=f"Pepe 0"
    )

    await client.save()

    for comm in comms:
        await client.communications.add(comm)

    print("Print client id: ", client.id)
  

if __name__ == "__main__":
    run_async(run())
