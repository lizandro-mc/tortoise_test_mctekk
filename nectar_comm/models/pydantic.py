
from tortoise.contrib.pydantic import (
    pydantic_model_creator,
    pydantic_queryset_creator
)

from models.relationship import (
    Client,
    Communication,
    Patient,
    Employee,
    Clinic
)


Client_Pydantic = pydantic_model_creator(Client)
Client_Pydantic_List = pydantic_queryset_creator(Client)
Communication_Pydantic = pydantic_model_creator(Communication)
Communication_Pydantic_list = pydantic_queryset_creator(Communication)
Patient_Pydantic = pydantic_model_creator(Patient)
Employee_Pydantic = pydantic_model_creator(Employee)
Clinic_Pydantic = pydantic_model_creator(Clinic)
