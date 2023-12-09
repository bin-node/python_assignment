numbers = []
physics = numbers.append(int(input('Please input the marks of physics: ')))
chemistry = numbers.append(int(input('Please input the marks of Chemistry: ')))
biology = numbers.append(int(input('Please input the marks of biology: ')))
mathematics = numbers.append(int(input('Please input the marks of mathematics: ')))
computer = numbers.append(int(input('Please input the marks of computer: ')))
percentage = sum(numbers) / len(numbers)
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print('Grade E')
else:
    print('Grade F')