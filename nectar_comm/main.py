
from tortoise import Tortoise, run_async
from tortoise.query_utils import Prefetch

# Models imports
from nectar_comm.models.relationship import (
    Client,
    Communication
)


async def reset_db():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()


async def run():
    await reset_db()
    client1 = await Client.create(id=1024, name="client1")
    await Communication.create(communication="communication 1 eyes", client_id=client1.id)

    communication_clients = await Communication.filter(communication="communication 1 eyes").values("created_at", "client__name")
    print(communication_clients[0])

    await Communication.create(communication="comunication 2 head", client=client1)
    client_with_filtered = (
        await Client.all()
        .prefetch_related(Prefetch("communications", queryset=Communication.filter(communication="communication 1 eyes")))
        .first()
    )
    client_without_filtered = await Client.first().prefetch_related("communications")
    print(len(client_with_filtered.communications))
    print(len(client_without_filtered.communications))

    client2 = await Client.create(id=2048, name="Client2")
    await Communication.all().update(client=client2)
    communication = await Communication.first()
    print(communication.client_id)


if __name__ == "__main__":
    run_async(run())
