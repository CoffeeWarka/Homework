first_string = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_string = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_string if len(word) > 5]
second_result = [(first_str_word, sec_str_word) for first_str_word in first_string for sec_str_word in second_string
                 if len(first_str_word) == len(sec_str_word)]
third_result = {word: len(word) for word in (first_string + second_string) if len(word) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)