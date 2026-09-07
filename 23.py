salary = float(input("Enter your salary: "))
bonus_percent = float(input("Enter bonus percentage: "))

annual = salary * 12
bonus = annual * bonus_percent / 100

print ("Annual Salary:", annual)
print ("Bonus Amount:", bonus) 

employees = {}

n = int(input("Enter number of employees: "))
for i in range(n):
    emp_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    emp_name = input("Enter employee name: ")
    emp_salary = float(input("Enter employee salary: "))
    employees[emp_id] = (department, emp_name, emp_salary)
print ("Employees:", employees)