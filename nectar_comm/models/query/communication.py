from models.nectar_relationship_models import Communication as Relations


class Communication(Relations):
    class Meta:
        table = "communications"
        table_description = "Saved all info and type of contact with the patient"
