# sdfdfff
arr = ['caaa', 'bbb', 'ccc', 'ddd']
# 非纯函数
arr.sort()
print(arr)
# 纯函数
print(sorted(arr))

print(arr)
print(arr[0])
print(arr[-1])
arr.reverse()
arr.append("sss")
arr.insert(0, '000')
del arr[1]
arr.pop()
arr.pop(-1)
print(arr)
arrlen = len(arr)
print(arrlen)
print("begin print arr")
for a in arr:
    print(a)
print(range(1, 5))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
for d in digits[2:6]:
    print(d)

#切片
print(digits[:3])
print(digits[1:3])

#列表生产式
res=[x * x for x in range(1, 11)]
print(res)
