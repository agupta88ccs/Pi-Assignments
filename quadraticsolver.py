# Quadratic Solver 
# Written by Asha Gupta 

def quadSolve(a,b,c):#function that inputs the three number in equation
        import math

        disc=b**2-4*a*c #discriminant formula

        if disc < 0:#if the discriminant is less than 0 no real roots
                print("No real roots")
                return ["No real roots"]
        elif disc == 0:#if zero
                return [-b/(2*a)] #return formula w/o the discriminant
        else:
                return [(-b-math.sqrt(disc))/(2*a),(-b+math.sqrt(disc))/(2*a)]#quadratic formula

print("Enter the coefficients for quadratic formula")
a =int(input("Enter a: ")) #puts in inputs for (a,b,c)
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(quadSolve(a,b,c))#print result
