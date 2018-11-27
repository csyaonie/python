from collections import Iterable
dic = {'color': 'red', 'point': 5}
print(dic['color'])

print(dic.get('color'))

print('第一个循环')
for key, value in dic.items():
    print(key + ':' + str(value))

dic.pop('color')

print('第二个循环')
for key, value in dic.items():
    print(key + ':' + str(value))

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


print(isinstance('abc', Iterable))   # str是否可迭代

print(isinstance([1, 2, 3], Iterable))  # list是否可迭代

print(isinstance(123, Iterable))   # 整数是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


