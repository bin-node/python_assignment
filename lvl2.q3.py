arr = [1,5,7,-1]
k = 6
possible_combination = []
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        a = arr[i] , arr[j]
        print(a)
        if sum(a) == k:
         possible_combination.append(a)
print(possible_combination)
