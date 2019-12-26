print ("\n\nWelcome to the special recruitment program, please answer the following questions: \n\n" )



cv = {}


cv['name'] = input("what is your name ?  ")

year = int(input("How old are you ?  "))
cv['age'] = year 

experience = int(input("How many years of experience do you have ?   "))
cv['experience'] = experience

cv['skills'] = []


print ("\n\n skills: \n\n ")
print ("1. python \n")
print ("2. c++ \n ")
print ("3. javascript \n ")
print ("4. juggling \n ")
print ("5. running \n ")
print ("6. Eating \n ")


skill_number1 = int(input ("choose a skill from above by entering its number:  "))
skill_number2 = int(input ("choose another a skill from above by entering its number:  ")) 


skills = ["python","design","presention","leadership","selfies","eating"]


cv['skills'].append(skills[skill_number1 - 1 ])
cv['skills'].append(skills[skill_number2 - 1 ])

if ( 25 < cv['age'] < 40  ) and ( cv['experience'] > 3 ) and "python" in cv['skills']:
	print (" \n\n you have been accpted ,   " , cv['name'] )
else:
    print (" \n\n unfortunatly " , cv['name'] , "  you do not fit the criteria > ")	



