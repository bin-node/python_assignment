def run_length(my_string):
    n = len(my_string)
    i = 0
    while i < n:
        count = 1
        while (i < n - 1 and my_string[i] == my_string[i + 1]):
            count += 1
            i += 1
        i += 1
        print(my_string[i - 1] +
              str(count),
              end="")


code = ("wwwwaaadebbbbbw")
run_length(code)