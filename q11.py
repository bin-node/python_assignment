
def count_digit(str):
    count = 0
    for i in str:
        count += int(i)
    return count
my_num = input("please enter your sample input: ")
num = count_digit(my_num)
print(f' Sample output: sum of digits = {num}')

final_num = count_digit(str(num))
print(f' final output: {final_num}')