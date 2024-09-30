def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [1, 'String', True]
values_dict = {'a': 2, 'b': 'да', 'c': False}

print_params(*value_list)
print_params(**values_dict)

values_list_2 = [1, 3.14]
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
