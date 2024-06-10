'''
Countdown module
'''
x = input ("Input number: ")

try:
    x = int(x)
except ValueError:
    print("That's not a number")
else:
    while x > 0:
        print(x)
        x = x - 1
    print("End")


def adding(first, second):
    '''
    Addition module
    '''
    try:
        result = int(first) + int(second)
        return result
    except ValueError:
        return "Invalid input. Please enter valid numbers."
firstnum = input("Input first number: ")
secondnum = input("Input second number: ")
print(adding(firstnum, secondnum))
