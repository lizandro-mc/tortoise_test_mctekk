
from tortoise import Tortoise, run_async
from tortoise.query_utils import Prefetch

# Query Models imports

from nectar_comm.models.query.client import Client
from nectar_comm.models.query.clinic import Clinic
from nectar_comm.models.query.communication import Communication
from nectar_comm.models.query.employee import Employee
from nectar_comm.models.query.patient import Patient

async def reset_db():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()


async def run():
    await reset_db()
    client1 = await Client.create(id=1024, name="client_1")
    clinic1 = await Clinic.create(id=1025, name="clinic_1")
    patient1 = await Patient.create(id=1026, name="patient_1")
    employee1 = await Employee.create(id=1027, name="employee_1")

    await Communication.create(
        communication="communication 1 eyes", 
        client_id=client1.id, 
        clinic_id = clinic1.id,
        patient_id = patient1.id, 
        employee_id = employee1.id
    )

    communication_clients = await Communication.filter(communication="communication 1 eyes").values("communication_type", "client__name")
    print(communication_clients[0])

    await Communication.create(
        communication="comunication 2 head", 
        client=client1,
        clinic = clinic1,
        patient = patient1, 
        employee = employee1
    )
    
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
    Client.query_test()


if __name__ == "__main__":
    run_async(run())
