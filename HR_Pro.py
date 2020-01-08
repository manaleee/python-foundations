from datetime import date

class Employee:
    def __init__ (self,name,age,salary,employemnt_year):
        self.name = name 
        self.age = age
        self.salary = salary
        self.employemnt_year = employemnt_year


    def get_work_year(self):
        return date.today().year - int(self.employemnt_year)


    def __str__(self):  
        return f"name: {self.name},   age: {self.age},  salary: {self.salary}, working year: {self.get_work_year()}"
    #  return   print ("name:  %s,  age: %s,  salary:  %s , working year:  %s "  % (self.name, self.age, self.salary, self.get_work_year())) 


class Manager(Employee):
    def __init__(self,name,age,salary,employemnt_year,bonus_percentage):
        super().__init__(name,age,salary,employemnt_year)
        self.bonus_percentages = bonus_percentage


    def get_bonus(self):
        return float(self.bonus_percentages) * float(self.salary)

    def __str__(self):
        #return   print ("name:  %s,  age: %s,  salary:  %s , working year:  %s , bonus: %f"  % (self.name, self.age, self.salary, self.get_work_year(), self.bonus))
        return f"name: {self.name},   age: {self.age},  salary: {self.salary}, working year: {self.get_work_year()}, bonus: {self.get_bonus()}"






employees = []
managers = []

print('\nWelcome to HR Pro 2019\n')
print ("""
            Options:
            1. Show Employees
            2. Show Managers
            3. Add An Employee
            4. Add A Manager
            5. Exit
    """)

print ()



choice = int(input("what would you like to do, my master ? "))

while choice != 5:
    if choice == 1:
        for employee in employees:
            print (employee)

    elif choice == 2:
        for manager in managers:
            print(manager)

    elif choice == 3:
        name = input("name: ")
        age = input("age: ")
        salary = input("salary: ")
        employemnt_date = input("employemnt_date: ")
        employee_obj = Employee(name,age,salary,employemnt_date)
        employees.append(employee_obj)

    elif choice == 4:
        name = input("name: ")
        age = input("age: ")
        salary = input("salary: ")
        employemnt_date = input("employemnt_date: ")
        bonus = input("bonus: ")
        employee_obj = Manager(name,age,salary,employemnt_date,bonus)
        managers.append(employee_obj)

    
    print('\n\nWelcome to HR Pro 2019\n')
    print ("""
            Options:
            1. Show Employees
            2. Show Managers
            3. Add An Employee
            4. Add A Manager
            5. Exit
         """)

    print ()
    choice = int(input("\nwhat would you like to do, my master ? \n"))

