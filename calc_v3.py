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


print(f'działanie:  {operation}')
print(f'obliczam : {first} {operation} {secondnum}')
print(f'wynik: {switchfun(operation, firstnum, secondnum)}')
