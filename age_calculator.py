from datetime import date 


def check_birthdate(year1,month1,day1):
	today = date.today() 

	if today.year > year1.year:
	   return print('the birthdate is invalid ')

	if today.year < year1.year:
	   return calculate_age(year1,month1,day1)
     


def calculate_age(year1,month1,day1):
	today = date.today()
	#age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
	age = today.year - year1.year - ((today.month, today.day) < (month1.month, day1.day))
    print (" you are  "  ,  age , "  years old. " )






year = int(input('Enter year of birth:   '))
month = int(input('Enter month of birth:   '))
day = int(input('Enter day of birth:   '))

check_birthdate(year,month,day)



