# Function to check if x is power of 2
def check_power(num):
    num = num/2
    if num == 2:
        return True
    elif num > 2:
        return check_power(num)
    else:
        return False
my_num = int(input("Please enter the number you like to check: "))
print(f'is the number power of two ? {check_power(my_num)}')