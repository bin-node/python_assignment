my_string = input("Please enter your string")
num = 0
str = 0
for i in my_string:
    if i.isdigit():
        num +=1
    else:
        str += 1
print(f'Alphabets: {str} & Number:{num}')