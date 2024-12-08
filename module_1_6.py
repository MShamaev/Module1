my_dict = {'понедельник': -5, 'вторник': -8, 'среда': 0, 'четверг': -3}
print(my_dict)
print(my_dict['среда'])
print(my_dict.get('пятница', 'нет данных'))
my_dict.update({'суббота': -11, 'воскресенье': -12})
thursday = my_dict.pop('четверг')
print(thursday)
print(my_dict)
my_set = {0, 'zero', 7.222, 0}
print(my_set)
my_set.update([True, (1, 'abc')])
my_set.remove(0)
print(my_set)