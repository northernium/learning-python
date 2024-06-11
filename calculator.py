'''
Calculator Module
'''
print('Welcome to the python calculator V.2')
print('Now this calculator has been upgraded to be able to operate with more than 2 numbers')
print('Just type "done" when you finish to see the result')

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
    if opr == '+':
        return add(f, s)
    elif opr == '-':
        return substrac(f,s)
    elif opr == '*':
        return multiple(f, s)
    elif opr == '/':
        return devide(f, s)
    else:
        return None

while True: #Added while loop so user can input more than just one number
    num1 = input('input number: ')
    if num1 == 'done':
        break
    try:
        x = result(x, num1)
    except NameError:
        None

    opr = input('input operation: ')
    if opr == 'done':
        break

    num2 = input('input number: ')
    if num2 == 'done':
        break

    try:
        x = result(x, num2)
    except NameError:
        x = result(num1, num2)

    opr = input('input operation: ')
    if opr == 'done':
        break

print ('result :' , x)
