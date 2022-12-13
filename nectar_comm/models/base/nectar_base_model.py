from tortoise.models import Model
from tortoise import fields
from enum import Enum


class NectarBaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Named():
    name = fields.CharField(max_length=100, null=True)


class ClientBaseModel(Named, NectarBaseModel):
    class Meta:
        table = "clients"
        table_description = "Saved all info about the client"


class ClinicBaseModel(Named, NectarBaseModel):
    class Meta:
        table = "clinics"
        table_description = "Saved all info about the clinic"


class EmployeeBaseModel(Named, NectarBaseModel):
    class Meta:
        table = "employees"
        table_description = "Saved all info about the employee"


class PatientBaseModel(Named, NectarBaseModel):
    class Meta:
        table = "patient"
        table_description = "Saved all info about the patient"


class CommunicationType(str, Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"
    IN_PERSON = "IN_PERSON"
    FAX = "FAX"
    VERBAL = "VERBAL"
    # Deprecated
    TEXT = "TEXT"


class CommunicationBaseModel(NectarBaseModel):
    #: Communication text
    communication = fields.CharField(max_length=500, null=True)

    #: Date of contact with patient
    contact_datetime = fields.DatetimeField(auto_now=True, null=True)

    #: Type of communicatication
    communication_type: CommunicationType = fields.CharEnumField(
        CommunicationType, default=CommunicationType.EMAIL)

    class Meta:
        table = "communications"
        table_description = "Saved all info and type of contact with the patient"
