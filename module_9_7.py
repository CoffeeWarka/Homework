def is_prime(func):
    def wrapper(*args):
        prime = True
        sum_three_result = func(*args)
        if sum_three_result <= 1:
            prime = False
        for i in range(2, int(sum_three_result ** 0.5) + 1):
            if sum_three_result % i == 0:
                prime = False
        if prime:
            return f'Простое\n{sum_three_result}'
        else:
            return f'Составное\n{sum_three_result}'
    return wrapper


@is_prime
def sum_three(*args):
    result = 0
    for i in args:
        result +=i
    return result


result = sum_three(2,3,6)
print(result)