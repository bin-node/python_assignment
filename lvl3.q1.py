file1 = open('doc.txt', 'r')
content = file1.readline().split()
for i in content:
    if len(i) % 2 == 0:
        print(i)
