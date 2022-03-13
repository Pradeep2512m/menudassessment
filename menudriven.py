import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("employee.db")


List_Of_Tables = connection.execute("Select name from sqlite_master Where type='table' And name='EMPLOYEE'").fetchall()

if List_Of_Tables != []:

    print("Table not found! ")
else:
    connection.execute('''CREATE TABLE EMPLOYEE(
                      ID INTEGER PRIMARY KEY AUTOINCREMENT,
                      EMPLOYEECODE INTEGER,
                      EMPLOYEENAME TEXT,
                      EMPLOYEEPHONE INTEGER,
                      EMPLOYEEEMAIL TEXT,
                      EMPLOYEEDESIGNATION TEXT,
                      EMPLOYEESALARY INTEGER,
                      EMPLOYEECOMPANYNAME TEXT

);''')

print("Table Created Successfully  !!! ")

while True:
    print("Select an OPTION from the MENU: ? ")

    print("1. ADD an Employee ")
    print("2. VIEW all the Employee ")
    print("3. SEARCH an Employee using an Employee Name ")
    print("4. UPDATE an Employee using an Employee Code ")
    print("5. DELETE an Employee using an Employee Code ")
    print("6. DISPLAY all the Employees with their GREATER than 50000 ")
    print("7. COUNT of all Employees ")
    print("8. DISPLAY all the Employee Details of RANGE and ALPHABETICAL ORDER ")
    print("9. DISPLAY all the Employee Details with SALARY with Less than AVG SALARY ")
    print("10. Exit ")

    choice = int(input("Enter any Choice to Selected  "))

    if choice == 1:

        getemployeecode = input("Enter The Employee Code: ")
        getemployeename = input("Enter the EmployeeName: ")
        getphone = input("Enter the EmployeePhone: ")
        getemail = input("Enter the EmployeeEmail: ")
        getdesignation = input("Enter the EmployeeDesignation: ")
        getsalary = input("Enter the EmployeeSalary: ")
        getcompanyname = input("Enter the CompanyName: ")

        result = connection.execute("Insert into EMPLOYEE(EMPLOYEECODE, EMPLOYEENAME, EMPLOYEEPHONE, EMPLOYEEEMAIL, EMPLOYEEDESIGNATION, EMPLOYEESALARY, EMPLOYEECOMPANYNAME) Values("+getemployeecode+", '" + getemployeename + "'," + getphone + ",'" + getemail + "','" + getdesignation + "'," + getsalary + ",'" + getcompanyname + "')")

        connection.commit()

        print("Employee data inserted Successfully")

    elif choice == 2:

        result = connection.execute("select * from EMPLOYEE")

        table = PrettyTable(["Empployee ID", "Employee Code", "EmployeeName", "Employee Phone", "Employee Email", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 3:

        getEmployeeName = input("enter the Employee_name to be search: ")

        result = connection.execute("select * from Employee where employeename= '" + getEmployeeName + "'")

        table = PrettyTable(["Empployee ID", "Employee Code", "EmployeeName", "Employee Phone", "Employee Email", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 4:

        getemployee_code = input("Enter the Employee code to update: ")


        getemployee_name = input("Enter the Employee name:")
        getphone = input("Enter the Employee phone no:")
        getemail = input("Enter the Employee email:")
        getdesignation = input("Enter the Employee designation:")
        getsalary = input("Enter the Employee salary:")
        getcompany_name = input("Enter the Company name:")

        result = connection.execute("Update EMPLOYEE set EMPLOYEENAME= '" + getemployee_name + "',EMPLOYEEPHONE= " + getphone + ",EMPLOYEEEMAIL= '" + getemail + "',EMPLOYEEDESIGNATION= '" + getdesignation + "', EMPLOYEESALARY=" + getsalary + ",EMPLOYEECOMPANYNAME= '" + getcompany_name + "' Where EMPLOYEECODE=" + getemployee_code)

        connection.commit()

        print("Employee data updated successfully")

    elif choice == 5:

        getemployee_code = input("enter the Employee code to deleted: ")

        connection.execute("Delete from EMPLOYEE Where EMPLOYEECODE=" + getemployee_code)

        connection.commit()

        print("Employee data deleted successfully")


    elif choice == 6:

        result = connection.execute("Select * from EMPLOYEE Where EMPLOYEESALARY > 50000")

        table = PrettyTable(["Empployee ID", "Employee Code", "EmployeeName", "Employee Phone", "Employee Email", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 7:

        result = connection.execute("select count(*) as employees from EMPLOYEE")
        for i in result:
            print("count of all employees:", i[0])

    elif choice == 8:

        lower_range = input("enter the lower range: ")
        higher_range = input("enter the higher range: ")
        result = connection.execute("select * from EMPLOYEE where EMPLOYEESALARY Between " + lower_range + " AND " + higher_range + " order by EMPLOYEESALARY asc")

        table = PrettyTable(["Employee ID", "Employee Code", "EmployeeName", "Employee Phone", "Employee Email", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 9:

        result = connection.execute("select * from EMPLOYEE where EMPLOYEESALARY<(select Avg(EMPLOYEESALARY) from EMPLOYEE)")

        table = PrettyTable(["Employee ID", "Employee Code", "EmployeeName", "Employee Phone", "Employee Email", "Employee Designation", "Employee Salary", "Employee Company Name"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 10:

        connection.close()

        break

    else:

        print("Invalid Choice !!! ")




