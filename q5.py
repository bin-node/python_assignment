num = int(input("please enter your number: "))
facto = 1
if num == 0 or num == 1:
    facto = 1
else:
    for i in range(1, num +1):
     facto = facto * i

print(facto)