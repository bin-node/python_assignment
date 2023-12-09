def find_divisor(num):
    pos_div = []
    for i in range(1, num):
        if num % i == 0:
         pos_div.append((i))
    return pos_div
num1 = int(input("please enter your number: "))
div_num1= find_divisor(num1)
num2 = int(input("please enter your second number: "))
div_num2 = find_divisor(num2)
lcm = 1
for i in div_num1:
    if i in div_num2:
        lcm *= i
print(f'LCM of 12 and 18 is: {lcm}')