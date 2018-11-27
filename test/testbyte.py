# Created by zyf on 2018/11/27.
b1='abc'.encode('ascii')
b2='我是你爸爸'.encode('utf-8')
print(b1)
print(b2)
print(b'abc'.decode('utf-8'))
print(b'\xe6\x88\x91\xe6\x98\xaf\xe4\xbd\xa0\xe7\x88\xb8\xe7\x88\xb8'.decode('utf-8'))
print(ord('A'));print(ord('中'));print(chr(66)); print(chr(25991))#整数与字符的转换
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') #忽略错误