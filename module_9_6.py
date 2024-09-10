from itertools import permutations
def all_variants(text):
    i = 0
    while i < len(text):
        for j in range(len(text)-i):
            yield text[j:j+i+1]

        i += 1

a = all_variants("abc")
for i in a:
    print(i)