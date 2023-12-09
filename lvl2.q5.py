def weather(list):
    avg = (sum(list)/ len(list))
    highest = max(list)
    lowest = min (list)
    print(f"Average temperature: {avg}")
    print(f"Highest Temperature: {highest}")
    print(f"Lowest Temperature: {lowest}")
my_data = weather([25,28,21,24,27])