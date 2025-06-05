temperatures = \
    [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
     22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def func(x):
    return x > 28


new_list = list(filter(func, temperatures))
n = len(new_list)

print(new_list)
print(f' самая высокая температура {max(new_list)}'
      f'\n самая низкая температура {min(new_list)}'
      f'\n средняя температура {int(sum(new_list) / n)}')


result = ' '.join(str(x) if x > 28 else '' for x in temperatures).split()
result = ' '.join(result)
new_list_map = list(map(int, result.split()))
print(new_list_map)
