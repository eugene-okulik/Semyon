my_tuple = ('text', 'list', False, 12, 15, 5)
my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last', 'last2']
my_dict_data = {
    'one': 'value', 
    'two': 'value2', 
    'three': 'value3', 
    'four': False, 
    'five': [1, 5, 8], 
    'six': {1, 6, 9}
}
my_set = {1, 3, 6,  None, 'text', False, 2.42, 3, 7}

my_dict = {
    'tuple': my_tuple,
    'list': my_list,
    'dict': my_dict_data,
    'set': my_set
}

print(my_dict['tuple'][-1])

my_list.append(13)
my_list.pop(1)

my_dict_data['i am a tuple'] = 'No'
my_dict_data.pop('i am a tuple')

my_set.add(1234)
my_set.pop()  # Удаляем случайный элемент

print(my_dict)



