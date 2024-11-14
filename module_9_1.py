def apply_all_func(int_list, *functions):

    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)

    return result

int_list = [1, 2, 3, 4, 5]
functions = [min, max, len, sum, sorted]

results = apply_all_func(int_list, *functions)

print(results)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))