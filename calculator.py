'''
Calculator Module
'''
print('Welcome to the python calculator')
print('Disclaimer: This calculator only work for 2 number')

def add(f,s):
    '''Add'''
    try:
        return int(f) + int(s)
    except ValueError:
        return 'Invalid Number'

def substrac(f,s):
    '''Substrac'''
    try:
        return int(f) - int (s)
    except ValueError:
        return 'Invalid Number'

def devide(f,s):
    '''Devide'''
    try:
        return int(f) / int (s)
    except ValueError:
        return 'Invalid Number'

def multiple(f,s):
    '''Multiplication'''
    try:
        return int(f) * int (s)
    except ValueError:
        return 'Invalid Number'

def result(f,s):
    '''Calculation'''
    if operation == '+':
        return add(f, s)
    elif operation == '-':
        return substrac(f,s)
    elif operation == '*':
        return multiple(f, s)
    elif operation == '/':
        return devide(f, s)
    else:
        return None

firstnum = input('Input the first number: ')
operation = input('Input the operation: ')
secondnum = input('Input the second number: ')
print("Result: ", result(firstnum, secondnum))
