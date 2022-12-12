
from tortoise import Tortoise, run_async

# Models imports
from nectar_comm.communication import Communication
from nectar_comm.client import Client


async def reset_db

async def run():

    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["__main__"]})
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