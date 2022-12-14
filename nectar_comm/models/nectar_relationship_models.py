from tortoise import fields
from nectar_comm.models.base.clinic import ClinicBaseModel
from nectar_comm.models.base.employee import EmployeeBaseModel
from nectar_comm.models.base.patient import PatientBaseModel
from nectar_comm.models.base.client import ClientBaseModel
from nectar_comm.models.base.communication import CommunicationBaseModel


"""
    Note: Working the relations in the same file allows to avoid the problems with the import cycle in python
"""

class Clinic(ClinicBaseModel):
    communications: fields.ReverseRelation["Communication"]


class Employee(EmployeeBaseModel):
    communications: fields.ReverseRelation["Communication"]


class Patient(PatientBaseModel):
    communications: fields.ReverseRelation["Communication"]


class Client(ClientBaseModel):
    communications: fields.ReverseRelation["Communication"]


class Communication(CommunicationBaseModel):
    client: fields.ForeignKeyRelation[Client] = fields.ForeignKeyField(
        "models.Client", related_name="communications", to_field="id"
    )
    clinic: fields.ForeignKeyRelation[Clinic] = fields.ForeignKeyField(
        "models.Clinic", related_name="communications", to_field="id"
    )
    employee: fields.ForeignKeyRelation[Employee] = fields.ForeignKeyField(
        "models.Employee", related_name="communications", to_field="id"
    )
    patient: fields.ForeignKeyRelation[Patient] = fields.ForeignKeyField(
        "models.Patient", related_name="communications", to_field="id"
    )
