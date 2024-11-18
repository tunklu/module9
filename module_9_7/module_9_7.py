from curses import wrapper

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        k = 0
        for i in range(2, result // 2 + 1):
            if (result % i == 0):
                k = k + 1
        if (k <= 0):
            print("Число простое")
        else:
            print("Число не является простым")
        return result
    return wrapper

@is_prime
def sum_three(*args):
    result = 0
    for num in args:
        result += num
    return result

#Пример:
result = sum_three(2, 3, 6)
print(result)