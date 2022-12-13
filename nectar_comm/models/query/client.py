from models.nectar_relationship_models import Client as Relations


class Client(Relations):
    class Meta:
        table = "clients"
        table_description = "Saved all info about the client"

    @staticmethod
    def query_test():
        print("Query test!")