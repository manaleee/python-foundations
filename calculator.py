num1 = input("\nEnter the first number:    ")
num2 = input("\nEnter the second number:    ")

number1 = int(num1)
number2 = int(num2)


if num1 != number1 or num2 != number2:
	print ('\n\nthe numbers were invalid , please run the program again ')


#if num1 = number1 and num2 = number2:
#	number1 = int(num1)
#	number2 = int(num2)


operation = input("\nchoose the operation (+,-,/,*) :    ")


#if operation != '+' or operation != '-' or operation != '/' or operation != '*' :
#	print ('\n\nthe operation is not valid. ,please run the program again ')

if operation == '+':
    answer = number1 + number2
    print ('\n\nthe answer is   ', answer )

elif operation == '-':
    answer = number1 - number2
    print ('\n\nthe answer is   ', answer )  

elif operation == '*':
    answer = number1 * number2
    print ('\n\nthe answer is   ' ,  answer )  

elif operation == '/':
    answer = number1 / number2
    print ('\n\nthe answer is   ' , answer )  

else:
    print ('\n\nthe operation is not valid. ,please run the program again ')








