from tortoise import fields
from tortoise.contrib.pydantic import (
    pydantic_model_creator,
    pydantic_queryset_creator
)
from enum import Enum
from nectar_comm.models.communication_relationship import Communication as Relations


class CommunicationType(str, Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"
    IN_PERSON = "IN_PERSON"
    FAX = "FAX"
    VERBAL = "VERBAL"
    # Deprecated
    TEXT = "TEXT"


class Communication(Relations):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)
    #: Communication text
    communication = fields.CharField(max_length=500, null=True)
    #: Date of contact with patient
    contact_datetime = fields.DatetimeField(auto_now=True, null=True)
    #: Type of communicatication
    communication_type: CommunicationType = fields.CharEnumField(
        CommunicationType, default=CommunicationType.EMAIL)


Communication_Pydantic = pydantic_model_creator(Communication)
Communication_Pydantic_list = pydantic_queryset_creator(Communication)
