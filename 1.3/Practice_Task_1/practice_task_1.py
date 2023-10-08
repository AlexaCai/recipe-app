a = input("Enter a number: ")
b = input("Enter an operator between + or -: ")
c = input("Enter another number: ")
a = int(a)
c = int(c)

operator_input = b

if b == "+":
    print("The sum of these numbers is", a + c)

elif b == "-":
    print("The substraction of these numbers is", a - c)

else:
    print ("You've entered a wrong operator, please choose between + or -")