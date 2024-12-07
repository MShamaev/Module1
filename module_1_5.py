immutable_var = (5, 'days', False, 10.1)
print(immutable_var)
immutable_var[2] = True
immutable_var[-1] = -0.1
print(immutable_var)
mutable_list = [5, 'days', False, 10.1]
mutable_list[2] = True
mutable_list.append(-0.1)
print(mutable_list)