
# function print menu 
def print_menu():
	print ("\n options: \n")
	print ("    1. show Emplyees \n")
	print ("    2. show Manager  \n")
	print ("    3. add an Employee \n")
	print ("    4. add a Manager \n")
	print ("    5. Exit  \n\n ")

	return

#-----------------------------------------
# 1. 
def show_employees(Employee_list):
    print ("\n Emplyees \n ")
    print (Employee_list)
    print ( " \n ------------------- \n ")
    
    Employee_list
	#return Employee_list


#----------------------------------------
# 2. 
def show_manager(manager_list):
    print ("\n Manager \n ")
    print (manager_list)
    print ( " \n ------------------- \n ")
    
	#return manager_list
	#manager_list


#---------------------------------------
# 3. 
def add_employees(Employee_list):
    name = input("name:  : ")
    age = int(input("age:  "))
    salary = input("salary:   ")
    Employee_year = input("Employement year:   ")
    print ( " \n Employee added succefully \n ")
    print ( " ------------------------------- \n \n ")
    
    Employee_list
	#return Employee_list
    

#-------------------------------------
# 4. 
def add_manager(manager_list):
    name = input("name:   ")
    age = int(input("age:  "))
    salary = input("salary:   ")
    Employee_year = input("Employement year:   ")
    bonus_percentage = input("Bonus percentage:   ")
    print ( " \n Manager added succefully \n ")
    print ( " ------------------------------- \n \n ")

	#return manager_list
	#manager_list





#-------------------------------------
#-------------------------------------
# main program

print ("\n\nWelcome to HR Pro 2019  \n\n ")

Employee_list = []
manager_list = []

choice = int(input("what would you like to do ? " ))   

while (choice != 1 or choice != 2 or choice != 3 or choice != 4 or  choice != 5) :
	print_menu()

	choice = int(input("what would you like to do ? " )) 
	print ("--------------------------\n")
		

	if choice == 1:
	   Employee_list = show_employees(Employee_list)
	elif  choice == 2:
		manager_list = show_manager(manager_list)
	elif choice == 3:
	    Employee_list = add_employees(Employee_list)
	elif choice == 4:
		manager_list = add_manager(manager_list)
	elif choice == 5:
	    print ("\n\nExit\n\n")
	    break 
	else:
	    print ("Error : " , choice , " is not a menu option  \n\n\n\n\n" )
print ( " \n\n Exit \n\n  ")





