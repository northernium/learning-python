'''
Calculator Module
'''
print('Welcome to the python calculator V.2.5')
print('Just type "done" when you finish to see the result')

def add(f,s):
    '''Add'''
    try:
        return float(f) + float(s)
    except ValueError:
        return 'Invalid Number'

def substract(f,s):
    '''Substract'''
    try:
        return float(f) - float (s)
    except ValueError:
        return 'Invalid Number'

def devide(f,s):
    '''Devide'''
    if s == 0:
        return "Error divide by 0"
    try:
        return float(f) / float (s)
    except ValueError:
        return 'Invalid Number'

def multiple(f,s):
    '''Multiplication'''
    try:
        return float(f) * float (s)
    except ValueError:
        return 'Invalid Number'

opr = None
tot = 0
num = 0
calc = 0
while True: #Added while loop so user can input more than just one number
    if calc == 0:
        num = input('input number: ') ##Added total calculation for clarity
    else:
        num = input(f'{tot} {opr} ')
        if num == 'done':
            if calc == 0:
                print("no numbers entered")
                break

    try:
        num = float(num)
        calc = calc + 1
        if tot == 0:
            tot = num
        else:
            if opr == '+':
                tot = add(tot, num)
            elif opr == '-':
                tot = substract(tot,num)
            elif opr == '*':
                tot = multiple(tot, num)
            elif opr == '/':
                tot = devide(tot, num)
    except ValueError:
        print('invalid input')

    if opr == 'done':
        break

    if calc == 1:
        opr = input('input operation: ')
    elif calc > 1:
        opr = input(f'{tot} ')
        if opr == 'done':
            break

print ('result :' , tot)
print ('total calculation :' , calc)
