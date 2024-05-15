class Employee():

    def __init__(self, first_name, last_name, salario_anual):
        self.first_name = first_name
        self.last_name = last_name
        self.salario_anual = salario_anual

    def aumento(self, amount=5000):
        self.salario_anual += amount

    def salario(self):
        return self.salario_anual
