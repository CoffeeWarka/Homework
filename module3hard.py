def calculate_structure_sum(*args):
    sum_all = 0
    for i in args:
        if isinstance(i, int):
            sum_all += i
        elif isinstance(i, str):
            sum_all += len(i)
        elif isinstance(i, dict):
            numbers = dict.values(i)
            words = dict.keys(i)
            sum_all += sum(numbers)
            chars = 0
            for k in words:
                chars += len(k)
            sum_all += chars
        if isinstance(i, (tuple, list, set)):
            for j in i:
                sum_all += calculate_structure_sum(j)
    return sum_all


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)