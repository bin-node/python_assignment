def out_of_range(list):
    try:
        for i in range(0, (len(list)+1)):
            print(list[i])
    except IndexError:
        print("Please check your range of index there is a problem")

my_lst = [1,2,3,4,5]
out_of_range(my_lst)