file1 = open('demo.txt', 'r')
contents = file1.readlines()
count = 0
for content in contents:
    count += 1
print(count)