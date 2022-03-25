import unittest
import sqlite3 as sql

class testing_menudrivenDb(unittest.TestCase):
    def setUp(self):
        self.Name="loki"
        self.code="2534"
        self.connection=sql.connect("Employee.db")

    def tearDown(self):
        self.name=" "
        self.code=" "
        self.connection.close()
    def test_verify_employee_name(self):
        result=self.connection.execute("select Employee Name from Employee where Employee_Num="+self.Number)
        for i in result:
            fetchedemployeename=i[0]
        self.assertEqual(self.Name,fetchedemployeename)

    def test_verify_employee_name_2(self):
        result=self.connection.execute("select Employee Name from Employee where Employee_Num="+self.Number)
        for i in result:
            fetchedemployeename=i[0]
        self.assertEqual(self.Name,fetchedemployeename)

if __name__=="__main__":
    unittest.main()



