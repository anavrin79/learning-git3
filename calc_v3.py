import sys

operation = input("Podaj działanie [+,-,*,/]: ")

first = input("Podaj pierwszy składnik: ")
second = input("Podaj drugi składnik: ")

firstnum = float(first)
secondnum = float(second)

if operation == "+":
    print ("działanie: " + operation)
    result = firstnum + secondnum
    print ("Obliczam : ")
    print (str(first) + str(operation) + str(second) + " = " + str(result))

elif operation == "-":
    print ("działanie: " + operation)
    result = firstnum - secondnum
    print ("Obliczam : ")
    print (str(first) + str(operation) + str(second) + " = " + str(result))

elif operation == "*":
    print ("działanie: " + operation)
    result = firstnum * secondnum
    print ("Obliczam :")
    print (str(first) + str(operation) + str(second) + " = " + str(result))

elif operation == "/":
    print ("działanie: " + operation)
    result = firstnum / secondnum
    print ("Obliczam :")
    print (str(first) + str(operation) + str(second) + " = " + str(result))

