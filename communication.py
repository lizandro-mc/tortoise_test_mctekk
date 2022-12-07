from datetime import datetime, timezone
from enum import Enum
from typing import Optional

import pymongo
import strawberry
import beanie.exceptions
from loguru import logger
from fastapi.encoders import jsonable_encoder
from pydantic import Field

from app.utils.exception_handler import AppException
from app.utils.model_helper import (
    NectarBaseModel,
    NectarDocument,
    PyObjectId,
    get_utc_now,
)


@strawberry.enum
class CommunicationType(str, Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"
    IN_PERSON = "IN_PERSON"
    FAX = "FAX"
    VERBAL = "VERBAL"
    # Deprecated
    TEXT = "TEXT"


class CommunicationBase(NectarBaseModel):
    client_id: PyObjectId = Field(...)
    patient_id: PyObjectId = Field(...)
    employee_id: PyObjectId = Field(...)
    communication_type: Optional[CommunicationType] = Field(None)
    communication: Optional[str] = Field(None, max_length=24000)
    contact_datetime: Optional[datetime] = Field(None)


# DB: nectarDB, Collection: client_comms
class Communication(NectarDocument, CommunicationBase):
    communication_id: PyObjectId | None = Field(None, alias="_id")
    clinic_id: PyObjectId = Field(...)
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)

    class Settings:
        name = "client_comms"
        indexes = [
            pymongo.IndexModel(
                [
                    ("clinic_id", pymongo.ASCENDING),
                    ("client_id", pymongo.ASCENDING),
                ],
                name="clinic_id_client_id_idx",
            ),
        ]

    @staticmethod
    async def read_communications(
        clinic_id: strawberry.ID, patient_id: Optional[strawberry.ID] = None
    ) -> list["Communication"]:
        search_dict = {"clinic_id": PyObjectId(clinic_id)}

        if patient_id:
            search_dict["patient_id"] = PyObjectId(patient_id)

        return await Communication.find(search_dict).to_list()

    @staticmethod
    async def create_communication(
        communication_data: "Communication",
    ) -> "Communication":
        try:
            created_communication = await Communication.insert(communication_data)

            if created_communication.id is None:
                raise AppException.NotFoundError("Communication not created")

            created_communication.communication_id = created_communication.id

            return created_communication

        except pymongo.errors.DuplicateKeyError:
            raise AppException.ValidationError("Communication with id already exists")

    @staticmethod
    async def read_communication(communication_id: PyObjectId) -> "Communication":
        communication = await Communication.get(communication_id)

        if communication is None:
            raise AppException.NotFoundError(
                f"Communication {communication_id} not found"
            )

        return communication

    @staticmethod
    async def update_communication(
        communication_id: PyObjectId, communication_update: "Communication"
    ) -> "Communication":
        Communication.parse_obj(communication_update.to_json())
        try:
            updated_communication = await communication_update.replace()
            return updated_communication
        except ValueError as e:
            logger.error(f"{e}")
            raise AppException.ValidationError(f"{e}")
        except beanie.exceptions.DocumentNotFoundError:
            logger.info(f"Communication {communication_id} not found")
            raise AppException.ValidationError(
                f"Communication {communication_id} not found"
            )

    @staticmethod
    async def delete_communication(communication_id: PyObjectId) -> True:
        communication = await Communication.find_one({"_id": communication_id})

        if communication is None:
            raise AppException.NotFoundError(
                f"Communication {communication_id} not found"
            )

        await communication.delete()
        return True


def serialize_communication(communication) -> dict:
    communication.updated_at = communication.updated_at.replace(tzinfo=timezone.utc)
    communication.created_at = communication.created_at.replace(tzinfo=timezone.utc)
    communication.contact_datetime = communication.contact_datetime.replace(
        tzinfo=timezone.utc
    )
    communication = jsonable_encoder(communication)

    return {
        "clinic_id": str(communication["clinic_id"]),
        "client_id": str(communication["client_id"]),
        "patient_id": str(communication["patient_id"]),
        "employee_id": str(communication["employee_id"]),
        "communication_id": str(communication["_id"]),
        "communication_type": communication["communication_type"],
        "communication": communication["communication"],
        "contact_datetime": str(communication["contact_datetime"]),
        "created_at": communication["created_at"],
        "updated_at": communication["updated_at"],
    }
