from tortoise import fields
from tortoise.models import Model

"""
    Note: Working the relations in the same file allows to avoid the problems with the import cycle in python
"""

class Clinic(Model):
    communications: fields.ReverseRelation["Communication"]


class Employee(Model):
    communications: fields.ReverseRelation["Communication"]


class Patient(Model):
    communications: fields.ReverseRelation["Communication"]


class Client(Model):
    communications: fields.ReverseRelation["Communication"]


class Communication(Model):
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
