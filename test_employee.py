import unittest
import requests
from unittest.mock import patch
import employee_testing as emp_test
from employee_testing import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = emp_test.Employee("John", "Doe", 50000)
        self.emp_2 = emp_test.Employee("Jane", "Smith", 60000)
    def tearDown(self):
        pass
    def test_email(self):
        
        self.assertEqual(self.emp_1.email, "John.Doe@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

        self.emp_1.first = "Ram"
        self.emp_2.first = "Sita"

        self.assertEqual(self.emp_1.email, "Ram.Doe@email.com")
        self.assertEqual(self.emp_2.email, "Sita.Smith@email.com")
    def test_fullname(self):
        self.emp_1 = emp_test.Employee("John", "Doe", 50000)
        self.emp_2 = emp_test.Employee("Jane", "Smith", 60000)
        self.assertEqual(self.emp_1.fullname, "John Doe")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

        self.emp_1.first = "Ram"
        self.emp_2.last = "Sita"

        self.assertEqual(self.emp_1.fullname, "Ram Doe")
        self.assertEqual(self.emp_2.fullname, "Jane Sita")
    def test_apply_raise(self):
        self.emp_1 = emp_test.Employee("John", "Doe", 50000)
        self.emp_2 = emp_test.Employee("Jane", "Smith", 60000)
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

        self.emp_1.raise_amt = 1.10
        self.emp_2.raise_amt = 1.20

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 57750)
        self.assertEqual(self.emp_2.pay, 75600)
    def test_monthly_schedule(self):
        with patch('employee_testing.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('January')
            
            
            mock_get.assert_called_with("http://company.com/John.Doe/January")
            self.assertEqual(schedule, 'Success')
            
if __name__ == '__main__':
    unittest.main()