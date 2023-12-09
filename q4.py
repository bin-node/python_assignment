start_num = int(input("Please enter the starting number: "))
stop_num = int(input("Please enter the end number: "))
my_numbers = list (range(start_num, stop_num+1))
odd_number = []
for i in my_numbers:
    if i % 2 != 0:
        odd_number.append(i)
print(f'Sum of odd numbers {sum(odd_number)}')