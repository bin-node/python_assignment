
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password == 'Bin-ode' and username == 'Binod':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

