from nectar_comm.models.nectar_relationship_models import Patient as Relations


class Patient(Relations):
    class Meta:
        table = "patients"
        table_description = "Saved all info about the patient"
