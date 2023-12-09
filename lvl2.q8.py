def vowel_count(my_str):
    count = 0
    for i in my_str:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


my_input = input("please enter your sentence: ")
total_vowel = vowel_count(my_input.lower())
print(f'Number of vowels: {total_vowel}')
