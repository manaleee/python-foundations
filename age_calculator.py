from datetime import date 


def check_birthdate(year1,month1,day1):
    today = date.today() 


    if today.year < year1:
        return False

    if today.year > year1:
       return True
     


def calculate_age(year1,month1,day1):
    today = date.today()
    #age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age = today.year - year1 - ((today.month, today.day) < (month1, day1))
    print (" you are  ", age, "  years old. " )

    





year = int(input('Enter year of birth:   '))
month = int(input('Enter month of birth:   '))
day = int(input('Enter day of birth:   '))

if check_birthdate(year,month,day) == True:
    calculate_age(year, month, day)
else:
    print("The birthdate is invalid.")



