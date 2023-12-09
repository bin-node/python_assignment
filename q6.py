def find_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append((i))
    return divisors
num = int(input("please enter your number: "))
num_div = find_perfect(num)
if sum(num_div) == num:
    print("The entered number is a perfect number")
else:
    print("Not a perfect number")