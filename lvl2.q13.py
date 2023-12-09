input_string = input("Please enter your string: ")
given_string = input("Please enter your given string: ")

x = lambda a, b: True if a[0] == b[0] else False
print(x(input_string, given_string))
