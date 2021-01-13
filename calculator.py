# Calculator 
# Written by Asha Gupta

# Define our function

def doMath(num1, num2, op):
	if op == 1:#For the first operator do the following
		result = num1+num2
	elif op == 2:
		result = num1-num2
	elif op == 3:
		result = num1*num2
	elif op == 4:
		result =round(num1/num2,2)#result in two decimal places
	elif op == 5:
		result = num1%num2
	return str(result)#shows the result as a string

#Input two numbers as integers
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

#Print each equation with input numbers
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
