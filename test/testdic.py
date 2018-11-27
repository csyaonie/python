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
