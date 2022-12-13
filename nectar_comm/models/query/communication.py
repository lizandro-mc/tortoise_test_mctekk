from nectar_comm.models.nectar_relationship_models import Communication as Relations


class Communication(Relations):
    class Meta:
        table = "communications"
        table_description = "Saved all info and type of contact with the patient"
    
    @staticmethod
    def read_communications():
        pass

    @staticmethod
    async def create_communication():
        pass