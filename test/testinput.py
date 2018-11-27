age = input("age...")
print(age)
age = int(age)#注意这个input都是字符串
if age > 18:
    print('adult')
elif age > 9:
    print('teenager')
else:
    print('child')
