from tortoise import fields
from enum import Enum
from nectar_comm.models.base.nectar_base_model import NectarBaseModel


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
        