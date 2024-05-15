import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.emp = Employee("Paulo", "Martins", 50000)

    def test_increase_salary_0(self):
        self.assertEqual(50000, self.emp.salario())
        self.emp.aumento()
        self.assertEqual(55000, self.emp.salario())

    def test_increase_salary_1(self):
        self.assertEqual(50000, self.emp.salario())
        self.emp.aumento(10000)
        self.assertEqual(60000, self.emp.salario())


unittest.main()
