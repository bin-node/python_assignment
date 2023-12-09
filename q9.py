from collections import Counter
input_list = [1,2,3,4,1,2,3,4]
print(Counter(input_list))
#second method
input_list = [1,2,3,4,1,2,3,4]
count1 =input_list.count(1)
count2 =input_list.count(2)
count3 =input_list.count(3)
count4 =input_list.count(4)
print(f'Frequency count 1: {count1}, 2: {count2}, 3: {count3}, 4: {count4}')