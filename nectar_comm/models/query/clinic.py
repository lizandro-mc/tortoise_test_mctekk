from models.nectar_relationship_models import Clinic as Relations


class Clinic(Relations):
    class Meta:
        table = "clinics"
        table_description = "Saved all info about the clinic"
