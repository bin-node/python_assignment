def pile_maker(n):
    output_pile = []
    if n % 2 == 0:
        for i in range(1, n-1, 2):
            output_pile.append(i+1)
    else:
        for i in range(0, n-1, 2):
            output_pile.append((i+1))
    print(output_pile)


data = int(input("Please enter your stone pile: "))
pile_maker(data)
# Given question is so vague and inconsistent with output
# still this code renders the input out of the question
