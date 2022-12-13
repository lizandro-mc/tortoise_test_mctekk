from tortoise import fields
from base.nectar_base_model import NectarBaseModel

class Patient(NectarBaseModel):
    pass

class Clinic(NectarBaseModel):
    pass

class Employee(NectarBaseModel):
    pass

class Client(NectarBaseModel):
    name = fields.CharField(max_length=500, null=True)
    communications: fields.ReverseRelation["Communication"]
    class Meta:
        table = "clients"
        table_description = "Saved all info about the client"


class Communication(NectarBaseModel):
    #: Communication text
    communication = fields.CharField(max_length=500, null=True)
    #: Date of contact with patient
    contact_datetime = fields.DatetimeField(auto_now=True, null=True)
    client: fields.ForeignKeyRelation[Client] = fields.ForeignKeyField(
        "models.Client", related_name="communications", to_field="id"
    )
    class Meta:
        table = "communications"
        table_description = "Saved all info and type of contact with the patient"



