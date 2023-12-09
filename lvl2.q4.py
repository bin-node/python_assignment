def rotate_array(array, n, d):
    d = d % n
    for i in range(0, n):
        if i < d:
            print(array[n + i - d], end=" ")
        else:
            print(array[i - d], end=" ")
    print("\n")


array = [1, 2, 3, 4, 5]
n = len(array)
d = 3

rotate_array(array, n, d)
