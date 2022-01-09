import sys

operation = input("Podaj działanie [+,-,*,/]: ")

first = input("Podaj pierwszy składnik: ")
second = input("Podaj drugi składnik: ")

firstnum = float(first)
secondnum = float(second)

def switchfun(operation, firstnum, secondnum):
    return {
        '+': firstnum + secondnum,
        '-': firstnum - secondnum,
        '*': firstnum * secondnum,
        '/': firstnum / secondnum,
    }[operation]

print ("działanie: " + operation)
print (f'Obliczam : {first} {operation} {secondnum} = {switchfun(operation, firstnum, secondnum)}')

