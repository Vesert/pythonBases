"""typeps of data"""

# Неизменяемые элементы
my_str = 'str'
my_num = 1
my_tuple = (2,3)

# Изменяемые элементы
my_list = [2,3,4]
my_dict = {'name' : 'Paul', 'What can i do' : 'I can wish you a happy birthday'}
my_set = set([2,3,2,5])

print('Тип числа ', my_num , str(type(my_num)))
print('Тип строки \'' + my_str + '\' ', str(type(my_str)))
print('Тип списка ', my_list, ' ',str(type(my_list)))
print('Тип кортежа ', my_tuple, ' ',str(type(my_tuple)))
print('Тип словаря ', my_dict, ' ',str(type(my_dict)))
print('Тип множества ', my_set, ' ',str(type(my_set)))

# Также есть объекты, но их рассмотрим отдельно

