from nectar_comm.models.nectar_relationship_models import Employee as Relations


class Employee(Relations):
    class Meta:
        table = "employees"
        table_description = "Saved all info about the employee"
