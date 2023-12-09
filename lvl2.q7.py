def calculate_median(my_list):
    if len(my_list) % 2 ==0:
        terms = my_list[(len(my_list)//2)-1] + my_list[(len(my_list)//2)]
        return terms/2
    else:
        return my_list[(len(my_list)//2)]


k = calculate_median([1,2,3,5,7,9])
print(k)