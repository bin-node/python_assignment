number = int(input("Enter a number: "))
rev = ''

while number > 0:
    last_digit = number % 10  # The remainder when it's divided by 10 will always be the last digit
    rev = rev + str(last_digit)
    number = number // 10

print("Reversed : ", rev)